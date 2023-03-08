import requests
import time
import random
import os

try:
    os.system('cls')
except:
    os.system('clear')

id = input("Enter Salon ID : ")

liste_de_mots = ["Hello how are you ? What's new ?", "What team will win this NBA season", "Moon is the only destination for this project", "2022 is Inevitable. Year of 2022 Is for metaverse. It would be fantastic. Strong vision, strong community. Strongly support this profect", "Cause i don't know your name bro", "Can u tell no ?", "now to bring it out", "How to connect wallet to megic Eden", "do vou finished study on boot camp on app?", "Hahaha.", "Maybe vou Joined when there was no timer. That's why man", "So when will your color change to guidian", "llets goo guys , hm 7 thanks bro I lets go I Where are vou from? Country Top Level project hard working team", "it's okay there will be more opportunities in the NFT spacel", "Parfect conmunity", "Have you guys eat your lunch?", "How many LGX do you have ?", "Except is LGX", "where we can invite ?", "how are u ?", "Hehe ok", ""]

duree = [180, 420] # Durée en secondes (3 minutes, 7 minutes)


while True :
    for mot in reversed(liste_de_mots):
        #mot_au_hasard = random.choice(mots)

        payload = {
            'content': f"{mot}"
        }

        header = {
            'authorization': 'OTg1MjMwNzQwMzUyNTMyNTYw.GeCgJJ.Zu9Vp0q4A7GpyQDmPDZi5Xo9StgO9ZVOdfTxcY'

        }

        r = requests.post(f"https://discord.com/api/v9/channels/{id}/messages", data=payload, headers=header)

        duree_au_hasard = random.choice(duree)

        time.sleep(duree_au_hasard)
