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
        if windll.user32.OpenClipboard(None):
            windll.user32.EmptyClipboard()
            windll.user32.CloseClipboard()
        
        while True:
            name = input("Anna ensin oma nimesi. Kirjoita \x1b[1mX\x1b[0m ja paina \x1b[1mENTER\x1b[0m peruuttaaksesi. ").capitalize()
            if name == "X":
                break
            elif (name not in namesnsongs.keys()) and len(name) > 1:
                break
            else:
                os.system('cls')
                print("Nimi jo annettu tai liian lyhyt, anna uudestaan.")
        
        if name == "X":
            break

        input("Anna seuraavaksi linkki biisin YouTube-videoon tai muu tieto, mistä biisi löytyy. \n Kun olet löytänyt biisin YouTubesta, kopioi osoite \x1b[1m(CTRL + C)\x1b[0m, sulje selain, ja liitä osoite tänne. \n Paina \x1b[1mENTER\x1b[0m avataksesi selaimen. ")
        open_browser()

        #Tyhjennetään leikepöytä

       

        info = input("Liitä \x1b[1m(CTRL + V)\x1b[0m osoite tai muu tieto tähän ja paina \x1b[1mENTER\x1b[0m. ")

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
        e = input("Paina\n -\x1b[1mENTER\x1b[0m hyväksyäksesi tiedot, piilottaaksesi tiedot ja siirtääksesi vuoron seuraavalle, \n-kirjoita \x1b[1mK\x1b[0m ja paina \x1b[1mENTER\x1b[0m antaaksesi omat tietosi uudestaan\n-tai jos olit viimeinen, kirjota \x1b[1mL\x1b[0m ja paina \x1b[1mENTER\x1b[0m aloittaaksesi pelin.\n \x1b[1mMUISTA SULKEA SELAIN!\x1b[0m ")
        if e == "k" or e == "K":
            continue
        elif e == "l" or e =="L":
            namesnsongs[name] = [song, info]
            break
        else:
            namesnsongs[name] = [song, info]
        os.system('cls')
        
    return namesnsongs

def colorize_tbl(olddata1, data2):
    data1 = olddata1.copy()
    # Colorize cell values
    for x in range(len(data1.columns)):
        for y in range(len(data1.index)):
            if data2.iloc[y, x]:
                data1.iloc[y, x] = f"\33[32m{data1.iloc[y, x]}\33[39m"  # Green
            else:
                data1.iloc[y, x] = f"\33[31m{data1.iloc[y, x]}\33[39m"  # Red
    
    # Colorize column headers
    org_cols = data1.columns
    new_cols = {col: f"\33[39m{col}\33[39m" for col in org_cols}
    data1.rename(columns=new_cols, inplace=True)  # Apply renaming in-place
    
    return data1

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
        input("Paina \x1b[1mENTER\x1b[0m kuunnellaksesi biisin.")
        info = namesnsongs[name][1]
        if "youtube.com" in info:
            open_browser(info)
        else:
            open_browser()
        input("Paina \x1b[1mENTER\x1b[0m jatkaaksesi.") 
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
        input("Paina \x1b[1mENTER\x1b[0m jatkaaksesi.")
        
        
        players.insert(0, players.pop())        
        os.system('cls')

    for col in guess_df.columns:
        print(f"Aika paljastaa, kenen biisivalinta oli \x1b[1m{col}\x1b[0m ja mikä on tarina biisin takana?")
        input("Paina \x1b[1mENTER\x1b[0m siirtyäksesi paljastamaan seuraava biisi!")
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
    colored_df = colorize_tbl(guess_df, rw)
    
    print(colored_df)
    print()
    print("Pisteet:")
    rw["Sum"] = rw[list(guess_df.columns)].sum(axis=1).astype(int)
    print(rw["Sum"].sort_values(ascending=False, inplace=False).to_string())
    print()

def run():
    os.system('cls')
    input("\x1b[1mElämäni biici\x1b[0m, v. 0.1, 2025. \nOhjelmointi: Jere Kyyrö \nTestaus: Antti Koskenalho, Sanna Kari\nPaina \x1b[1mENTER\x1b[0m aloittaaksesi.")
    os.system('cls')
    input("Aloitetaan biisien syöttämisellä. Kukin pelaaja syöttää itse biisinsä tiedot. Suosittelemme käyttämään kuulokkeita! Jatka painamalla \x1b[1mENTER\x1b[0m.")
    songs = {}
    while True:
        os.system('cls')
        songs = readsongs()
        joiner = ", "
        print(f"Pelaajat: {joiner.join(list(songs.keys()))}. ")
        if input("Paina \x1b[1mENTER\x1b[0m jatkaaksesi tai kirjoita \x1b[1mA +\x1b[0m \x1b[1mENTER\x1b[0m syöttääksesi pelaajien tiedot uudestaan.").capitalize() != "A":
            break
    os.system('cls')
    input("Biisit luettu! Paina \x1b[1mENTER\x1b[0m aloittaaksesi pelin!")
    show_and_guess(songs)

if __name__ == "__main__":
    
    run()

 



 








   

    