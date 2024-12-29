import os
import random
import pandas as pd

def readsongs(namesnsongs = {}):
    while True:
        name = input("Anna oma nimesi: ").capitalize()
        print(name)
        if name == "Valmis":
            break
        song = input("Anna artistin ja biisin nimi: ").capitalize()
        info = input("Anna lisätieto tai jätä tyhjäksi painamalla enteriä: ")
        os.system('cls')
        namesnsongs[name] = [song, info]
        print(f"{name}n biisi lisätty! Kirjoita \"valmis\" kun kaikki biisit on lisätty.")
    return namesnsongs

def show_and_guess(namesnsongs:dict):
    votes = {}
    players = list(namesnsongs.keys())
    shuffled = players.copy()
    random.shuffle(shuffled)
    os.system('cls')
    for i, name in enumerate(shuffled):
        songname = namesnsongs[name][0]
        songvotes = [] 
        print(f"Kuunnellaan biisi numero {i+1}:")
        print(songname)
        print(f"Lisätieto: {namesnsongs[name][1]}")
        input("Paina enter jatkaaksesi.")
        for pname in players:
            guess = input(f"{pname}, kenen biisi? ").capitalize()
            songvotes.append(guess)
        votes[songname] = songvotes
        print("Arvaustilanne:")
        situ = pd.DataFrame(votes)
        situ["Pelaaja"] = players
        situ = situ.set_index(["Pelaaja"])
        print(situ)
        input("Paina enter jatkaaksesi.")
        os.system('cls')

    situ = pd.DataFrame(votes)
    situ["Pelaaja"] = players
    situ = situ.set_index(["Pelaaja"])

    for col in situ.columns:
        print(f"Aika paljastaa, kenen biisivalinta oli {col}?")
        input("Paina enter siirtyäksesi eteenpäin!")
        os.system('cls')
        
    rw = situ.copy()
    
    for col in situ.columns:
        for row in situ.index:
            if namesnsongs[situ.loc[row,col]][0] == col:
                rw.loc[row,col] = True
            else:
                rw.loc[row,col] = False
    os.system('cls')
    rw["Sum"] = rw[list(situ.columns)].sum(axis=1).astype(int)
    print("Oikeat arvaukset:")
    print(rw["Sum"].sort_values(ascending=False, inplace=False).to_string())
    print()

if __name__ == "__main__":
    os.system('cls')
    songs = {}
    while True:
        songs = readsongs()
        if input("Paina mitä tahansa jatkaaksesi tai kirjoita \"a\" aloittaaksesi uudestaan.") != "a":
            break
    os.system('cls')
    input("Biisit luettu! Paina enter aloittaaksesi pelin!")
    show_and_guess(songs)