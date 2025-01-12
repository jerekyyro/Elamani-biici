import os
import random
import pandas as pd

def open_browser(url="youtube.com"):
    import webbrowser as wb

    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito"
    wb.get(chrome_path).open_new(url)

def readsongs(namesnsongs = {}):
    from ctypes import windll

    while True:
        
        while True:
            name = input("Anna ensin oma nimesi. Kirjoita X ja paina ENTER peruuttaaksesi. ").capitalize()
            if name == "X":
                break
            elif (name not in namesnsongs.keys()) and len(name) > 1:
                break
            else:
                os.system('cls')
                print("Nimi jo annettu tai liian lyhyt, anna uudestaan.")
        
        if name == "X":
            break

        input("Anna seuraavaksi linkki biisin YouTube-videoon tai muu tieto, mistä biisi löytyy. \n Kun olet löytänyt biisin YouTubesta, kopioi osoite (CTRL + C), sulje selain, ja liitä osoite tänne. \n Paina ENTER avataksesi selaimen. ")
        open_browser()

        #Tyhjennetään leikepöytä

        if windll.user32.OpenClipboard(None):
            windll.user32.EmptyClipboard()
            windll.user32.CloseClipboard()

        info = input("Liitä (CTRL + V) osoite tai muu tieto tähän ja paina ENTER. ")

        while True:
            song = input("Anna vielä artistin ja biisin nimi: ").capitalize()
            if len(song) > 3:
                break
            else:
                os.system('cls')
                print("Biisin nimi liian lyhyt, anna uudestaan.")

        os.system('cls')
        
        print("Antamasi tiedot:")
        print("Nimesi: ", name)
        print("Biisi: ", song)
        print("Osoite/lisätieto: ", info)
        e = input("Paina ENTER hyväksyäksesi tiedot, piilottaaksesi tiedot ja siirtääksesi vuoron seuraavalle, kirjoita K ja paina ENTER antaaksesi omat tietosi uudestaan tai jos olit viimeinen, kirjota L ja paina ENTER aloittaaksesi pelin.\n MUISTA SULKEA SELAIN! ")
        if e == "k" or e == "K":
            continue
        elif e == "l" or e =="L":
            namesnsongs[name] = [song, info]
            break
        else:
            namesnsongs[name] = [song, info]
        os.system('cls')
        
    return namesnsongs

def show_and_guess(namesnsongs:dict):
    players = list(namesnsongs.keys())
    shuffled = players.copy()
    random.shuffle(shuffled)
    guess_df = pd.DataFrame(index=players)
    os.system('cls')
    for i, name in enumerate(shuffled):
        songname = namesnsongs[name][0]
        guess_df[songname] = ""     
        print(f"Kuunnellaan biisi numero {i+1}:")
        print(songname)
        print(f"Linkki/lisätieto: {namesnsongs[name][1]}")
        input("Paina enter kuunnellaksesi biisin.")
        info = namesnsongs[name][1]
        if "youtube.com" in info:
            open_browser(info)
        else:
            open_browser()
        input("Paina enter jatkaaksesi.") 
        for pname in players:
            while True:
                joiner = ", "
                thislist = players.copy()
                thislist.remove(pname)
                guess = input( f"{pname}, kenen biisi? (Muut pelaajat: {joiner.join(thislist)}) " ).capitalize()
                if guess in thislist:
                    guess_df.loc[pname, songname] = guess
                    break
                else:
                    print("Virheellinen nimi, anna nimi uudestaan!")
        print("Arvaustilanne:")
        print(guess_df)
        input("Paina ENTER jatkaaksesi.")
        
        
        players.insert(0, players.pop())        
        os.system('cls')

    for col in guess_df.columns:
        print(f"Aika paljastaa, kenen biisivalinta oli {col} ja mikä on tarina biisin takana?")
        input("Paina enter siirtyäksesi paljastamaan seuraava biisi!")
        os.system('cls')
         
    rw = guess_df.copy()
    for col in guess_df.columns:
        for row in guess_df.index:
            if namesnsongs[guess_df.loc[row, col]][0] == col:
                rw.loc[row,col] = True
            else:
                rw.loc[row,col] = False
    os.system('cls')
    print("Oikeat arvaukset:")
    print(rw)
    print()
    print("Pisteet:")
    rw["Sum"] = rw[list(guess_df.columns)].sum(axis=1).astype(int)
    print(rw["Sum"].sort_values(ascending=False, inplace=False).to_string())
    print()

def run():
    os.system('cls')
    input("Elämäni biici, v. 0.1, 2025. \nOhjelmointi: Jere Kyyrö \nTestaus: Antti Koskenalho\nPaina ENTER aloittaaksesi.")
    os.system('cls')
    input("Aloitetaan biisien syöttämisellä. Kukin pelaaja syöttää itse biisinsä tiedot. Suosittelemme käyttämään kuulokkeita! Jatka painamalla ENTER.")
    songs = {}
    while True:
        os.system('cls')
        songs = readsongs()
        joiner = ", "
        print(f"Pelaajat: {joiner.join(list(songs.keys()))}. ")
        if input("Paina ENTER jatkaaksesi tai kirjoita A + ENTER syöttääksesi pelaajien tiedot uudestaan.").capitalize() != "A":
            break
    os.system('cls')
    input("Biisit luettu! Paina enter aloittaaksesi pelin!")
    show_and_guess(songs)

if __name__ == "__main__":
    run()

   

    