import sys, time

import models, util, view
from controller import controller
from data import *

def main():
    # view.welcome()
    # mode = view.main_menu()
    # mode = new || load || quit
    # gamestate = controller[mode]()

    # gamestate = controller["new"]()
    name = "Jao"
    player = models.Character(CHARACTER["type"], CHARACTER["integrity"], CHARACTER["description"], CHARACTER["inventory_limit"], name)
    hasKnife = False
    isGorillaAngry = True
    hasBanana = False
    hasBrigKey = False
    isPrisonerFreed = False
    hasChestKey = False
    hasTreasure = False
    areNativesHostile = False
    map1 = util.generate_map1(hasKnife, isGorillaAngry, hasBanana, hasBrigKey, areNativesHostile)
    map2 = util.generate_map2()
    gamestate = models.GameState(player, [CHARACTER_POS["x"], CHARACTER_POS["y"]], "map1", hasKnife, isGorillaAngry, hasBanana, hasBrigKey, isPrisonerFreed, hasChestKey, hasTreasure, areNativesHostile, [], [], map1, map2)

    while True:
        command = view.menu(gamestate)   
        action = command.split(" ")[0]
        view.clear()
        controller[action](gamestate, command)
    

if __name__ == "__main__":
    main()