import json
import os

money = 0
killed = 0
player_x = 0
player_y = 0
location = [0, 0]

def save_exists():
    return os.path.exists('save.txt')

def try_load_save():
    try:
        if os.path.exists('save.txt'):
            load()
        else:
            save()
    except:
        print("Error while loading the save!")

def save():
    global money, killed, player_x, player_y, location 
    saveData = json.dumps([money, killed, player_x, player_y, location])
    f = open('save.txt', 'w')
    f.write(saveData)

def load():   
    global money, killed, player_x, player_y, location  
    f = open('save.txt', 'r')
    jsonData = f.readline()
    jsonObject = json.loads(jsonData)
    money = jsonObject[0]
    killed = jsonObject[1]
    player_x = jsonObject[2]
    player_y = jsonObject[3]
    location = jsonObject[4]
