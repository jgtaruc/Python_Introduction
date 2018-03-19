import sys, time

import models
from data import *


def animate_text(text, t):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(t)


def generate_map1(hasKnife, isGorillaAngry, hasBanana, hasBrigKey, areNativesHostile):
    tile_kinds = MECHANICS["Tiles"]
    positions = MECHANICS["Positions"]
    outline = MECHANICS["Map1"]
    game_map = outline

    def getCoordInfo(x, y):
        if positions["Banana"]["x"] == x and positions["Banana"]["y"] == y:
            objs = []
            if not hasBanana:
                banana = ITEMS["Banana"]
                objs.append(models.Item(banana["type"], banana["integrity"], banana["description"], banana["name"]))
            return (tile_kinds["Banana_Tree"], objs)
        elif positions["CaptnQtr"]["x"] == x and positions["CaptnQtr"]["y"] == y:
            objs = []
            if not hasKnife:
                knife = ITEMS["Knife"]
                objs.append(models.Item(knife["type"], knife["integrity"], knife["description"], knife["name"]))
            if not hasBrigKey:
                key = ITEMS["BrigKey"]
                objs.append(models.Item(key["type"], key["integrity"], key["description"], key["name"]))
            return (tile_kinds["Captain_Quarters"], objs)
        elif positions["LadderUD"]["x"] == x and positions["LadderUD"]["y"] == y:
            return (tile_kinds["Top_Deck_Ladder"], [])
        elif positions["Wheel"]["x"] == x and positions["Wheel"]["y"] == y:
            return (tile_kinds["Ship_Wheel"], [])
        elif GORILLA_POS["x"] == x and GORILLA_POS["y"] == y and isGorillaAngry:
            return (tile_kinds["Empty"], [GORILLA])
        else:
            return (tile_kinds["Empty"], [])
        

    for x in range(0, MAP_WIDTH):
        for y in range(0, MAP_HEIGHT):
            isPassable = False
            res = getCoordInfo(x, y)
            tile_info = res[0]
            items = res[1]

            if outline[x][y] == 1:
                isPassable = True

            game_map[x][y] = models.Tile(tile_info["kind"], x, y, items, isPassable, tile_info["description_long"], tile_info["description_short"])
    
    return game_map


def generate_map2():
    tile_kinds = MECHANICS["Tiles"]
    positions = MECHANICS["Positions"]
    outline = MECHANICS["Map2"]
    game_map = outline

    def getCoordInfo(x, y):
        if positions["Brig"]["x"] == x and positions["Brig"]["y"] == y:
            return tile_kinds["Brig"]
        elif positions["CrgoHold"]["x"] == x and positions["CrgoHold"]["y"] == y:
            return tile_kinds["Cargo_Hold"]
        elif positions["LadderLD"]["x"] == x and positions["LadderLD"]["y"] == y:
            return tile_kinds["Bottom_Deck_Ladder"]
        elif positions["Galley"]["x"] == x and positions["Galley"]["y"] == y:
            return tile_kinds["Galley"]
        else:
            return tile_kinds["Empty"]
        

    for x in range(0, MAP_WIDTH):
        for y in range(0, MAP_HEIGHT):
            isPassable = False
            tile_info = getCoordInfo(x, y)

            if outline[x][y] == 1:
                isPassable = True

            game_map[x][y] = models.Tile(tile_info["kind"], x, y, [], isPassable, tile_info["description_long"], tile_info["description_short"])

    return game_map


def getTile(gamestate, x, y):
    currentMap = gamestate.map1
    if gamestate.currentMap == "map2":
        currentMap = gamestate.map2
    
    return currentMap[x][y]