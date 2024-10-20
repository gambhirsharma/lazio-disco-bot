import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import time

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
chat_id = os.getenv('CHAT_ID')
USER_ID = os.getenv('USER_ID')
PASS = os.getenv('PASS')

login_url = ('https://dirstudio.laziodisco.it/')
secure_url = ('https://dirstudio.laziodisco.it/Home/AccettazionePostoAlloggio')

payload = {
    'username': USER_ID,
    'password': PASS
}

fixed_h4_text = "Accettazione del Posto Alloggio"
fixed_h3_text = ("Gentile studente, lo status di idoneo al posto alloggio non le dà al momento "
                 "diritto ad un posto letto presso una delle residenze di Disco. Consulti frequentemente "
                 "il sito istituzionale di Disco e la sua area personale, per aggiornamenti in merito "
                 "a futuri scorrimenti di graduatoria e successive assegnazioni. Grazie")

# telegram bot part

def send_message(mess): 
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={mess}"
    
    r = requests.get(url)
    print(r.json())


def main(): 
    with requests.session() as s: 
        s.post(login_url, data=payload)
        r = s.get(secure_url)
        soup = BeautifulSoup(r.content, 'html.parser')
    
    h4_text = soup.find('h4', class_='text-center').get_text(strip=True)
    message_div = soup.find('div', style="text-align:center")
    h3_text = message_div.find('h3').get_text(strip=True)

    if h4_text == fixed_h4_text and h3_text == fixed_h3_text:
        send_message('No Update')
        # message through the bot that their is no update
        print('No update')
    else: 
        send_message("Check website there is some update!!")
        # message through the bot that their is an update
        h4_text_translated = GoogleTranslator(source='it', target='en').translate(h4_text)
        h3_text_translated = GoogleTranslator(source='it', target='en').translate(h3_text)
        print("H4 Text (Original):", h4_text)
        print("H4 Text (Translated):", h4_text_translated)
        print("H3 Text (Original):", h3_text)
        print("H3 Text (Translated):", h3_text_translated)
        print("Update detected!")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(1800)
