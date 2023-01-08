import os
from shutil import copyfile
from googlesearch import search

switch_files = []
newgrounds = []
directory = os.getcwd() # gets current file directory

appdata = os.getenv('LOCALAPPDATA') # gets appdata path location
gd = appdata + "\\GeometryDash\\" # gets the geometry dash song folder

def copy_and_replace(): # copies original file, renames, and deletes.
    print("\nCopying Original Song File...")
    copyfile(gd + str(song_id) + ".mp3", directory + "\\" + str(song_id) + "_copy.mp3")
    print("Swapping Old song with New...")
    copyfile(directory + "\\" + replace, gd + str(song_id) + ".mp3")
    os.remove(directory + "\\" + replace)
    os.rename(directory + "\\" + str(song_id) + "_copy.mp3", directory + "\\" + replace)

while True:
    try:
        song_type = str(input("Name or ID: ")).upper()
        break
    except:
        continue

while song_type:
    if song_type == "ID":
        while True:
            try:
                song_id = int(input("Song ID: ")) # gets the song id
                break
            except:
                print("\nSong File must be an integer.\n")
                continue
        if os.path.exists(gd + str(song_id) + ".mp3"): # checks if the song exist in the gd song folder
            print("\nSong File Found. [" + song_id + "]\n")
            break
        else:
            print("\nSong File not found. [" + song_id + "]\n")
            continue
    elif song_type == "NAME":
        while True:
            try:
                song_id = str(input("Song Name [Artist - Song name]: ")).replace("-", "") # gets the song from newgrounds
                for i in search(song_id + " newgrounds", num_results=1):
                    song_id = i.rsplit("/", 1)[-1]
                    break
                break
            except:
                print("\nIssue Finding Song.\n")
                continue
        if os.path.exists(gd + str(song_id) + ".mp3"): # checks if the song exist in the gd song folder
            print("\nSong File Found. [" + song_id + "]\n")
            break
        else:
            print("\nSong File not found. [" + song_id + "]\n")
            continue
    else:
        print("Error.")

for i in os.listdir(): # checks all files in directory
    if ".mp3" in i:
        switch_files.append(i) # adds files to the directory if they have the file extension ".mp3"


if len(switch_files) == 0: # checks if there is anything in the list
    print("No mp3 files found.\n")
else:
    search_term = str(input("Search Term [Leave Blank if None]: "))
    if search_term == "": # checks for a search term, if none then list all from the switch files list
        print("\nSong to Switch With: \n")
        search_term_found = True
        for i in switch_files:
            print(str(i))
    else: # if there is a search term, look for that search term and print the results
        print("\nSong to Switch With: \n")
        for i in switch_files:
            if search_term in i:
                print(str(i))
                search_term_found = True

if search_term_found == False:
    print("Audio with that name not found.")

while True:
    replace = str(input("\nFile to swap with: "))
    if (replace + ".mp3") in switch_files: # checks for the file that was specified
        replace = replace + ".mp3" 
        copy_and_replace()
        close = input("Done.")
        break
    elif (replace) in switch_files:
        copy_and_replace()
        close = input("Done.")
        break
    else:
        print("File with that name not found.")
        continue
