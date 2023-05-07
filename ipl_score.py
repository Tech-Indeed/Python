import requests
from bs4 import BeautifulSoup
import pywhatkit
import datetime

url= "https://www.cricbuzz.com/live-cricket-scores/66355/mi-vs-csk-49th-match-indian-premier-league-2023"
while True:

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    scored_card = soup.find("div", class_="cb-col cb-col-67 cb-scrs-wrp")
    score1 = scored_card.text
    current_time = datetime.datetime.now()
    Hour = current_time.hour
    Minute = current_time.minute + 1
    pywhatkit.sendwhatmsg_to_group("HHTlPW3CyJrEksgJwaPqlc", score1, Hour, Minute, 10, True, 2)




