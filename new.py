import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

# Define the URL
login_url = ('https://dirstudio.laziodisco.it/')
url = "https://dirstudio.laziodisco.it/Home/MessaggiDisco"

# Define the content to check against
fixed_card_title = "27 Giugno 2024"
fixed_card_text = "Attivazione nuova sezione per l'inserimento del documento di soggiorno"

def fetch_and_check_content():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the CardDisco section
    card_disco = soup.find("div", class_="row CardDisco")
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

# Main loop to run the script periodically
if __name__ == "__main__":
    while True:
        print("Checking for updates...")
        fetch_and_check_content()
        time.sleep(3600)  # Check every hour

