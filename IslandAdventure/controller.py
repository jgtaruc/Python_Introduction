import json, sys, time

import models, view, util
from data import *

def new():
    name = view.name_screen()
    player = models.Character(CHARACTER["type"], CHARACTER["integrity"], CHARACTER["description"], CHARACTER["inventory_limit"], name)
    hasKnife = False
    isGorillaAngry = True
    hasBanana = False
    hasBrigKey = False
    isPrisonerFreed = False
    hasChestKey = False
    hasTreasure = False
    areNativesHostile = False
    map1 = util.generate_map1()
    map2 = util.generate_map2()
    gamestate = models.GameState(player, [CHARACTER_POS["x"], CHARACTER_POS["y"]], "map1", hasKnife, isGorillaAngry, hasBanana, hasBrigKey, isPrisonerFreed, hasChestKey, hasTreasure, areNativesHostile, [], [], map1, map2)
    print "Starting game..."
    time.sleep(2)
    view.clear()
    view.intro()
    return gamestate


def load():
    print "load game"
    return
    

def gorillaFrame(gamestate, tile):
    goBack = False
    while not goBack:
        view.gorilla()
        commands = view.tile_menu()
        commands = commands.split(" ")
        if commands[0] not in MECHANICS["Frame_Verbs"]:
            view.clear()
            print "Invalid command!!!"
            time.sleep(1)
            view.clear()
        else:
            if commands[0] == "back":
                goBack = True
            view.clear()
            print "Invalid command!!!"
            time.sleep(1)
            view.clear()

        if commands[0] == "inventory":
            controller["inventory"](gamestate, commands)

        if commands[0] == "take":
            view.clear()
            print "There is nothing to take here"
            time.sleep(1)
            view.clear() 

        if commands[0] == "give":
            if len(commands) < 2:
                view.clear()
                print "You have given the gorilla nothing"
                time.sleep(1)
                view.clear() 

            if not inInventory(gamestate.character.inventory(), commands[1]):
                view.clear()
                print "Item not available in your inventory"
                time.sleep(1)
                view.clear() 
            
            if commands[1] == "banana":
                
            else:
                view.clear()
                print "The angry gorilla does not want it!!!"
                time.sleep(1)
                view.clear() 

        def give():
            return
        def take():
            return
        def search():
            return
        def unlock():
            return
        def sail():
            controller["sail"]()
    view.clear()


def tile_view(gamestate, tile):
    if tile.posx == GORILLA_POS["x"] and tile.posy == GORILLA_POS["y"] and GORILLA in tile.objects:
        gorillaFrame(gamestate, tile)
        


def move(gamestate, command):
    x = gamestate.characterPos[0]
    y = gamestate.characterPos[1]

    currentMap = gamestate.map1
    if gamestate.currentMap == "map2":
        currentMap = gamestate.map2

    directives = command.split(" ")
    if len(directives) < 2:
        return

    direction = directives[1].lower()
    if not direction in MECHANICS["Directions"]:
        view.clear()
        print "Invalid movement direction!!!"
        time.sleep(1)
        view.clear()
        return

    if direction == "north" or direction == "n":
        x -= 1
    elif direction == "east" or direction == "e":
        y += 1
    elif direction == "south" or direction == "s":
        x += 1
    elif direction == "west" or direction == "w":
        y -= 1

    if not currentMap[x][y].canGo:
        return

    # TODO
    # isVisited = [x, y] in gamestate.visitedTiles   
    # if not isVisited:
        # gamestate.visitedTiles.append([x,y])

    tile = util.getTile(gamestate, x, y)
    allow = tile_view(gamestate, tile)

    if allow:
        gamestate.characterPos = [x,y]    
    
    return


def inventory(gamestate, command):
    view.clear()
    view.inventory(gamestate) 
    view.clear()
    return


def take(gamestate, command):
    return

def search():
    return


def look(gamestate, command=None):
    view.clear()
    view.map1(gamestate, MECHANICS)         
    if gamestate.currentMap == "map1":
        print "X - Character"
        print "BT - Banana Tree"
        print "CQ - Captain's Quarters"
        print "LD - Ladder down to lower deck"
        print "G - Angry Gorilla"
        print "SW - Ship's Wheel"
    else:
        return

    print "\n"
    raw_input("Press [Enter] to exit this view...")
    view.clear()
    return


def eat():
    return


def cut():
    return


def cut():
    return


def unlock():
    return


def sail():
    return

def end(gamestate=None, command=None):
    if gamestate == None:
        print "Thank you for playing..."
        sys.exit(0)
    else:
        confirm = raw_input("Are you sure you want to quit? You will lose all your progress [Y/n]: ")
        if confirm.lower() == "y":
            print "Thank you for playing..."        
            sys.exit(0)
    return


controller = {
    "new": new,
    "load": load,
    "move": move,
    "inventory": inventory,
    "look": look,
    "quit": end
}