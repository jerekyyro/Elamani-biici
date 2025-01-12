import os
import random
import pandas as pd

def readsongs(namesnsongs = {}):
    while True:
        while True:
            name = input("Anna oma nimesi: ").capitalize()
            if (name not in namesnsongs.keys()) and len(name) > 1:
                break
            else:
                os.system('cls')
                print("Nimi jo annettu tai liian lyhyt, anna uudestaan.")
        while True:
            song = input("Anna artistin ja biisin nimi: ").capitalize()
            if len(song) > 3:
                break
            else:
                os.system('cls')
                print("Biisin nimi liian lyhyt, anna uudestaan.")
            
        info = input("Anna lisätieto tai jätä tyhjäksi painamalla enteriä: ")
        os.system('cls')
        
        
        print("Antamasi tiedot:")
        print("Nimesi: ", name)
        print("Biisi: ", song)
        print("Lisätieto: ", info)
        e = input("Paina ENTER hyväksyäksesi tiedot, piilottaaksesi tiedot ja siirtääksesi vuoron seuraavalle, K + ENTER antaaksesi omat tietosi uudestaan tai L + ENTER aloittaaksesi pelin.")
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
    votes = {}
    players = list(namesnsongs.keys())
    shuffled = players.copy()
    random.shuffle(shuffled)
    guess_df = pd.DataFrame(index=players)
    os.system('cls')
    for i, name in enumerate(shuffled):
        songname = namesnsongs[name][0]
        #songvotes = []
        guess_df[songname] = ""
     
        print(f"Kuunnellaan biisi numero {i+1}:")
        print(songname)
        print(f"Lisätieto: {namesnsongs[name][1]}")
        input("Paina enter jatkaaksesi.")
        for pname in players:
            while True:
                joiner = ", "
                thislist = players.copy()
                thislist.remove(pname)
                guess = input( f"{pname}, kenen biisi? (Muut pelaajat: {joiner.join(thislist)}) " ).capitalize()
                if guess in thislist:
                    #songvotes.append(guess)
                    guess_df.loc[pname, songname] = guess
                    break
                else:
                    print("Virheellinen nimi, anna nimi uudestaan!")
        #votes[songname] = songvotes
        print("Arvaustilanne:")
        #situ = pd.DataFrame(votes)
        #situ["Pelaaja"] = players
        #situ = situ.set_index(["Pelaaja"])
        #print(situ)
        print(guess_df)
        input("Paina enter jatkaaksesi.")
        
        
        #TÄMÄ RIKKOO NYT ARVAUSJÄRJESTYKSEN. KORJAA LUOMALLA DATAFRAME HETI ALUSSA, jonka idneksiksi asetetaan pelaajat; lisätään kolumni aina uuden biisin alussa, sitten 
        # kolumni, pelaaja -indeksin avulla arvaukset
        players.insert(0, players.pop())        
        os.system('cls')

    #situ = pd.DataFrame(votes)
    #situ["Pelaaja"] = players
    #situ = situ.set_index(["Pelaaja"])

    #for col in situ.columns:
    for col in guess_df.columns:
        print(f"Aika paljastaa, kenen biisivalinta oli {col}?")
        input("Paina enter siirtyäksesi paljastamaan seuraava biisi!")
        os.system('cls')
         
    #rw = situ.copy()
    rw = guess_df.copy()
    #for col in situ.columns:
    for col in guess_df.columns:
        #for row in situ.index:
        for row in guess_df.index:
            #if namesnsongs[situ.loc[row,col]][0] == col:
            if namesnsongs[guess_df.loc[row, col]][0] == col:
                rw.loc[row,col] = True
            else:
                rw.loc[row,col] = False
    os.system('cls')
    print("Oikeat arvaukset:")
    print(rw)
    print()
    print("Pisteet:")
    #rw["Sum"] = rw[list(situ.columns)].sum(axis=1).astype(int)
    rw["Sum"] = rw[list(guess_df.columns)].sum(axis=1).astype(int)
    print(rw["Sum"].sort_values(ascending=False, inplace=False).to_string())
    print()

if __name__ == "__main__":
    os.system('cls')
    input("Elämäni biici, v. 0.1, 2025. Paina mitä tahansa aloittaaksesi.")
    os.system('cls')
    songs = {}
    while True:
        songs = readsongs()
        joiner = ", "
        print(f"Pelaajat: {joiner.join(list(songs.keys()))}. ")
        if input("Paina mitä tahansa jatkaaksesi tai kirjoita \"a\" syöttääksesi pelaajien tiedot uudestaan.") != "a":
            break
    os.system('cls')
    input("Biisit luettu! Paina enter aloittaaksesi pelin!")
    show_and_guess(songs)


