# imports
from instagrapi import Client

import schedule
import time

# Functions
def add_post():
    bot = Client()

    bot.login(username="apenas_conta", password="Colinsd29@")
    album = ["img/note1.jpeg", "img/note.jpeg"]
    cap = "Teste \n#teste #conta"

    bot.album_upload(album, caption = cap)

schedule.every(1).minutes.do(add_post)

count = 0

while 1:
    schedule.run_pending()
    time.sleep(1)
    
    count+=1
    
    print("waiting ", count, " seconds")