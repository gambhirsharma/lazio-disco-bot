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
        s.post(login_url, data=payload)
        r = s.get(secure_url)
##############3# ai generated
        m = s.get(message_url)
        message_page = BeautifulSoup(m.content, 'html.parser')
        card_disco = message_page.find("div", class_="row CardDisco")
        print('compiler is hitting this')

    if not card_disco:
        print("CardDisco section not found.")
        return 

    # Find all cards within CardDisco
    card_titles = card_disco.find_all("h5", class_="card-title")
    card_texts = card_disco.find_all("p", class_="card-text")

    # Check if each title and text matches the expected fixed content
    for title, text in zip(card_titles, card_texts):
        card_title_text = title.get_text(strip=True)
        card_text_content = text.get_text(strip=True)

        if card_title_text != fixed_card_title or fixed_card_text not in card_text_content:
            print("Update detected!")
            print("Title:", card_title_text)
            print("Text:", card_text_content)
            return  # Stop checking further if an update is found
        else:
            print("No update detected.")

##############3# ai generated

        # soup = BeautifulSoup(r.content, 'html.parser')
        #
        # h4_text = soup.find('h4', class_='text-center').get_text(strip=True)
        # message_div = soup.find('div', style="text-align:center")
        # h3_text = message_div.find('h3').get_text(strip=True)
        # if h4_text == fixed_h4_text and h3_text == fixed_h3_text:
        #     # send_message('No Update')
        #     # message through the bot that their is no update
        #     status_message = 'No Update'
        #     save_log(status_message, timestamp)
        #     print('No update')
        # else:
        #     status_message = 'New Update!!'
        #     save_log(status_message, timestamp)
        #     # send_message("Check website there is some update!!")
        #     # message through the bot that their is an update
        #     h4_text_translated = GoogleTranslator(source='it', target='en').translate(h4_text)
        #     h3_text_translated = GoogleTranslator(source='it', target='en').translate(h3_text)
        #     print("H4 Text (Original):", h4_text)
        #     print("H4 Text (Translated):", h4_text_translated)
        #     print("H3 Text (Original):", h3_text)
        #     print("H3 Text (Translated):", h3_text_translated)
        #     print("Update detected!")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(3600)
