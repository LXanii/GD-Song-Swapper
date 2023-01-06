import os, shutil

switch_files = []
directory = os.getcwd() # gets current file directory

appdata = os.getenv('APPDATA') # gets appdata path location
for i in range(7): # this loop removes the ending of the file directory so we can add local later
    appdata = appdata[:-1]

appdata = appdata + "Local" # Described Above ^^^^
gd = appdata + "\\GeometryDash\\" # gets the geometry dash song folder

def copy_and_replace(): # copies original file, renames, and deletes.
    print("Copying Original Song File...")
    shutil.copyfile(gd + str(song_id) + ".mp3", directory + "\\" + str(song_id) + "_copy.mp3")
    print("Swapping Old song with New...")
    shutil.copyfile(directory + "\\" + replace, gd + str(song_id) + ".mp3")
    os.remove(directory + "\\" + replace)
    os.rename(directory + "\\" + str(song_id) + "_copy.mp3", directory + "\\" + replace)

while True:
    while True:
        try:
            song_id = int(input("Song ID: ")) # gets the song id
            break
        except:
            print("\nSong File must be an integer.\n")
            continue
    if os.path.exists(gd + str(song_id) + ".mp3"): # checks if the song exist in the gd song folder
        print("\nSong File Found\n")
        break
    else:
        print("\nSong File not found.\n")
        continue

for i in os.listdir(): # checks all files in directory
    if ".mp3" in i:
        switch_files.append(i) # adds files to the directory if they have the file extension ".mp3"
    
if len(switch_files) == 0: # checks if there is anything in the list
    print("No mp3 files found.\n")
else:
    print("Song to Switch With: \n" + str(switch_files))

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
