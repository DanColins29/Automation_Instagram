# imports
from instagrapi import Client

import schedule
import time

# Functions
def add_post():
    bot = Client()

    bot.login(username="bfalbertomersmann", password="*****")
    album = ["img/liberte.jpeg", "img/auto.jpeg"]
    cap = "Indicações de leitura do maranhense Padre João Mohana disponíveis para empréstimo.\n\nLiberte seu filho da insegurança e Autoanálise para o êxito profissional\n\nAgora me conta aí, qual desses vocês já conheciam ou que vai para sua lista de futura leitura?\n\n#leitura #bibliotecaiesma #iesma #padrejoaomohana #joaomohana #teologia"

    bot.album_upload(album, caption = cap)

schedule.every().wednesday.at("10:09").do(add_post)

count = 0

while 1:
    schedule.run_pending()
    time.sleep(1)
    
    count+=1
    
    print("waiting ", count, " seconds")