import requests
from requests.api import get
import boto3
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import time
from datetime import datetime
from botocore.exceptions import ClientError
import json

def get_secret():
    secret_name = "Lazio_disco_bot"
    region_name = "eu-south-1"
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    secret = get_secret_value_response['SecretString']
    return secret

secret = json.loads(get_secret())

USER_ID = secret['lazio_USER']
PASS = secret['lazio_pass']
TOKEN = secret['lazio_telegram_bot_token']
BOT_ID = secret['lazio_telegram_bot_id']
chat_id = secret['lazio_telegram_bot_chat_id']

login_url = ('https://dirstudio.laziodisco.it/')
secure_url = ('https://dirstudio.laziodisco.it/Home/AccettazionePostoAlloggio')
message_url = ('https://dirstudio.laziodisco.it/Home/MessaggiDisco')

payload = {
    'username': USER_ID,
    'password': PASS
}

fixed_h4_text = "Accettazione del Posto Alloggio"
fixed_h3_text = ("Gentile studente, lo status di idoneo al posto alloggio non le dà al momento "
                 "diritto ad un posto letto presso una delle residenze di Disco. Consulti frequentemente "
                 "il sito istituzionale di Disco e la sua area personale, per aggiornamenti in merito "
                 "a futuri scorrimenti di graduatoria e successive assegnazioni. Grazie")

fixed_card_title = "27 Giugno 2024"
fixed_card_text = "Attivazione nuova sezione per l'inserimento del documento di soggiorno"

def send_message(mess): 
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={mess}"
    r = requests.get(url)
    # print(r.json())

def save_log(status, timestamp):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('LazioDiscoLogs')

    if not timestamp:
        timestamp = datetime.utcnow().isoformat()

    try:
        table.put_item(
            Item={
                'LogId': f"log-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
                'Status': status,
                'Timestamp': timestamp
            }
        )
        print("Log saved successfully.")
    except Exception as e:
        print(f"Error saving log: {e}")



def lambda_handler(event, context):
    with requests.session() as s:
        try:
            s.post(login_url, data=payload)
            r = s.get(secure_url)

            # Check for CardDisco section before processing
            m = s.get(message_url)
            message_page = BeautifulSoup(m.content, 'html.parser')
            # card_disco = message_page.find("div", class_="row CardDisco")
            # if not card_disco:
            #     print("CardDisco section not found.")
            #     return
            card_titles = message_page.find_all("h5", class_="card-title", recursive=True)
            card_texts = message_page.find_all("p", class_="card-text")


            # Check card titles and texts
            for title, text in zip(card_titles, card_texts):
                card_title_text = title.get_text(strip=True)
                card_text_content = text.get_text(strip=True)

                if card_title_text != fixed_card_title or fixed_card_text not in card_text_content:
                    print("Update detected!")
                    print("Title:", card_title_text)
                    print("Text:", card_text_content)
                    status_message = 'New Update!!'
                    # TODO:

                    save_log(status_message, None)
                    send_message("Check website there is some update!!")

                    return {
                        'statusCode': 200,
                        'body': status_message,
                    }

            else:
                print("No update detected.")
                status_message = 'No Update'
                # TODO:

                # send_message(status_message)
                save_log(status_message, None)

                return {
                    'statusCode': 200,
                    'body': status_message
                }

        except Exception as e:
            print(f"An error occurred: {e}")
            # TODO:

            send_message("Error in bot")
            save_log("Error", None)

# if __name__ == "__main__":
#     lambda_handler(None, None)
