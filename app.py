# imports
from enum import Flag
from instagrapi import Client

import schedule
import time

# Functions
def add_post():
    bot = Client()

    bot.login(username = user, password = pwd)
    album = ["img/liberte.jpeg", "img/auto.jpeg"]
    cap = "Indicações de leitura do maranhense Padre João Mohana disponíveis para empréstimo.\n\nLiberte seu filho da insegurança e Autoanálise para o êxito profissional\n\nAgora me conta aí, qual desses vocês já conheciam ou que vai para sua lista de futura leitura?\n\n#leitura #bibliotecaiesma #iesma #padrejoaomohana #joaomohana #teologia"

    bot.album_upload(album, caption = cap)

# Variables
count = 0
flag = False
user = "apenas_conta"
pwd = "Colinsd29@"

# Call Function By Schedule
schedule.every().wednesday.at("11:33").do(add_post)

# Loop
while (flag == False):
    schedule.run_pending()
    time.sleep(1)
    
    count+=1
    
    print("waiting ", count, " seconds")