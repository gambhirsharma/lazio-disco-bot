import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import time
import csv
import os
from dotenv import load_dotenv
from datetime import datetime
# import boto3


load_dotenv()

TOKEN = os.getenv('TOKEN')
chat_id = os.getenv('CHAT_ID')
USER_ID = os.getenv('USER_ID')
PASS = os.getenv('PASS')

login_url = ('https://dirstudio.laziodisco.it/')
secure_url = ('https://dirstudio.laziodisco.it/Home/AccettazionePostoAlloggio')
message_url = ("https://dirstudio.laziodisco.it/Home/MessaggiDisco")
# message_url = ('http://127.0.0.1:8080/index.html')

payload = {
    'username': USER_ID,
    'password': PASS
}

fixed_h4_text = "Accettazione del Posto Alloggio"
fixed_h3_text = ("Gentile studente, lo status di idoneo al posto alloggio non le dà al momento "
    "diritto ad un posto letto presso una delle residenze di Disco. Consulti frequentemente "
    "il sito istituzionale di Disco e la sua area personale, per aggiornamenti in merito "
    "a futuri scorrimenti di graduatoria e successive assegnazioni. Grazie")

# for message_url
fixed_card_title = "27 Giugno 2024"
fixed_card_text = "Attivazione nuova sezione per l'inserimento del documento di soggiorno"


# telegram bot part
# telegram bot part

def send_message(mess):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={mess}"

    r = requests.get(url)
    print(r.json())

def save_log(status, timestamp):
        with open('update_log.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, status])



def main():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
                    # Uncomment and modify for Telegram message
                    send_message("Check website there is some update!!")
                    status_message = 'New Update!!'
                    save_log(status_message, timestamp)
                    break  # Stop checking after first update

            else:
                print("No update detected.")
                status_message = 'No Update'
                save_log(status_message, timestamp)

        except Exception as e:  # Handle potential exceptions
            print(f"An error occurred: {e}")
            send_message("Error in bot")



if __name__ == "__main__":
    while True:
        main()
        time.sleep(3600)
