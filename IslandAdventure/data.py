import json 

import models

MAP_WIDTH = 12
MAP_HEIGHT = 12
TEXT_ANIMATION = 0#0.025

MECHANICS = json.load(open("gameMechanics.json"))
CHARACTER = MECHANICS["Character"]
CHARACTER_POS = MECHANICS["Positions"]["Character"]
TILES = MECHANICS["Tiles"]
ITEMS = MECHANICS["Items"]

GORILLA_POS = MECHANICS["Positions"]["Gorilla"]
GORILLA_DATA = MECHANICS["Gorilla"]
GORILLA = models.Gorilla(GORILLA_DATA["type"], GORILLA_DATA["integrity"], GORILLA_DATA["description"], GORILLA_DATA["name"], GORILLA_DATA["dialog"], GORILLA_DATA["alt_dialog"])