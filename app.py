# imports
from instagrapi import Client

import schedule
import time

# Functions
def add_post():
    bot = Client()

    bot.login(username="apenas_conta", password="****")
    album = ["img/note1.jpeg", "img/note.jpeg"]
    cap = "Teste \n#teste #conta"

    bot.album_upload(album, caption = cap)

schedule.every(5).minute.do(add_post)

while 1:
    schedule.run_pending()
    time.sleep(1)