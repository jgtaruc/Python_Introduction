import time, os, sys

import util
from data import *

def welcome():
    welcome_str = [
        "==================================================",        
        "  *******",
        " *********        **       ***        *** ********",
        "***              ****      ** **    ** ** **",
        "***    ****    ***  ***    ** **    ** ** ******",
        "***      **   **********   **  **  **  ** **",
        " **********  ****    ****  **   ****   ** **",
        "   *******  ****      **** **    **    ** ********",
        "==================================================",
        "|                 Island Adventure               |",
        "=================================================="
    ]
    for s in welcome_str:
        print s
        time.sleep(0.05)

    raw_input("Press [Enter] to continue...")
    clear()
    return


def main_menu():
    s = None
    while True:
        print "[1] New Game"
        print "[2] Load Game"
        print "[q] Quit"
        s = raw_input("> ")
        if s == "1" or s == "2" or s == "q":
            break
        clear()
        print "Please enter one of the following:"

    if s == "1":
        mode = "new"
    elif s == "2":
        mode = "load"
    else:
        mode = "quit"
    
    clear()

    return mode


def name_screen():
    print "Please enter your name:"
    name = raw_input("> ")
    clear()
    return name


def intro():
    message = MECHANICS["Premise"]
    for c in message:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(TEXT_ANIMATION)
    print "\n"

    for i in range(0, 3):
        sys.stdout.write(".\n")
        sys.stdout.flush()
        time.sleep(1)
    print "\n"

    message = MECHANICS["IntroText"] + "\n\n" + MECHANICS["IslandText"]
    for c in message:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(TEXT_ANIMATION)
    print "\n"

    raw_input("Press [Enter] to continue...")
    return


def menu(gamestate):
    while True:
        map1(gamestate, MECHANICS)                 
        print "============== Available commands: ==============="
        print "move/go [n, north, e, east, s, south, w, west]"
        print "inventory"
        print "take <item>"
        print "give <item>"
        print "drop <item>"
        print "search"
        print "look"
        print "cut"
        print "sail"
        print "save"
        print "load"
        print "quit"
        print "==================================================="
        command = raw_input("> ")
        temp = command.split(" ")[0]
        if temp in MECHANICS["Verbs"]:
            break
        else:
            clear()
            print "Invalid command!!!"
            time.sleep(1)
            clear()

    return command


def tile_menu():               
    print "============== Available commands: ==============="
    print "inventory"
    print "take <item>"
    print "give <item>"
    print "drop <item>"
    print "search"
    print "cut"
    print "sail"
    print "back"
    print "==================================================="
    command = raw_input("> ")

    return command
    
def inventory(gamestate):
    print "===================== Inventory: =====================\n"
    if len(gamestate.character.inventory()) == 0:
        print "You have nothing..."
    else:
        for item in gamestate.character.inventory():
            print "%s - %s" % (item.name(), item.description)
    print "\n======================================================"
    print "\n"
    raw_input("Press [Enter] to exit your inventory")
    return


def objectives(gamestate):
    return


def tile_information(gamestate):
    return


def gorilla():
    gorilla_str = [
        "        ********",
        "     **************",
        "  ******************** ",
        " ***   \        /   ***",
        " ***   0\\      /0   ***",
        " ***       o o      ***",
        "  **        |       **",
        "  **    v=======v   **",
        "   **  |         | **",
        "    *** ^=======^ ***",
        "      *************"
    ]
    for s in gorilla_str:
        print s

    print "\n"
    print "Gorilla: ",
    util.animate_text(GORILLA.talk(), TEXT_ANIMATION)
    print "\n"

    util.animate_text("An angry Gorilla is blocking your path towards the ship's wheel.", TEXT_ANIMATION)
    print "\n"    
    util.animate_text("Maybe it wants something because it is reaaally grumpy.", TEXT_ANIMATION)
    print "\n"


def banana_tree(alt):
    if not alt: 
        banana_str = [
            "              /\\",
            "          /\\ /  \\ /\\",
            "          \\ \\   // /",
            "           \ jjjj /",
            "           V|    |V",
            "            |    |",
            "            |    |",
            "            |    |",
            "============|    |==============",
            "     \     //||||\\\\        /",
            "      \                   /",
            "       ==================="
        ]
    else:
        banana_str = [
            "",
            "",
            "",
            "",
            "             ____",
            "            |    |",
            "            |    |",
            "            |    |",
            "============|    |==============",
            "     \     //||||\\\\        /",
            "      \                   /",
            "       ==================="
        ]
    for s in banana_str:
        print s


def captains_quarters(alt):
    if not alt:
        captains_quarters_str = [
            "=============Captain's Quarters============",
            "    =====",
            "   /   O \\",
            "   \~~~~~/           ________",
            "    =====           /        \\",
            "                    |________|",
            "    ============    /~~~~~~~~/|",
            "    |knife     |   /        /|/",
            "    ============  /________//",
            "     |_|----|_|   |_|~~~~|_|",
            "",
            "============================================"
        ]
    else:
        captains_quarters_str = [
            "=============Captain's Quarters============",
            "    =====",
            "   /   O \\",
            "   \~~~~~/           ________",
            "    =====           /        \\",
            "                    |________|",
            "    ============    /~~~~~~~~/|",
            "    |          |   /        /|/",
            "    ============  /________//",
            "     |_|----|_|   |_|~~~~|_|",
            "",
            "============================================"
        ]

    for s in captains_quarters_str:
        print s


def brig(alt):
    if not alt:
        brig_str = [
            "   [===============Brig==============]",
            "   ||  ||   ||   ||   ||   ||   ||  ||",
            "   ||  ||   ||   ||   ||   ||   ||  ||",
            "   ||  ||   ||   ||___||___||   ||  ||",
            "   ||prisoner|   ||   ||   ||   ||  ||",
            "   ||(-_-)  ||   ||   ||  o||   ||  ||",
            "   || -|-   ||   ||   ||   ||   ||  ||",
            "   || / \   ||   ||   ||   ||   ||  ||",
            "  /==================================/",
            " /                                  /",
            "/                                  /"
        ]
    else:
        brig_str = [
            "   [===============Brig==============]",
            "   ||  ||   ||   ||   ||   ||   ||  ||",
            "   ||  ||   ||   ||   ||   ||   ||  ||",
            "   ||  ||   ||   ||___||___||   ||  ||",
            "   ||  ||   ||   / |       ||   ||  ||",
            "   ||  ||   ||   |o|       ||   ||  ||",
            "   ||  ||   ||   | |       ||   ||  ||",
            "   ||  ||   ||   | |       ||   ||  ||",
            "  /===================(-_-)===========/",
            " /                     -|-           /",
            "/                      / \          /"
        ]

    for s in brig_str:
        print s


def galley():
    galley_str = [
        "==============Galley================="
        "",
        "",
        "                        /\ <(o )  /\\",
        "                        \_\(    )/_/",
        "                            |  |",
        "                           -m--m-----",
        "                                   ||",
        "                                   ||",
        "                                   ||",
        "                                  ===="
    ]

    for s in galley_str:
        print s


def cargo_hold(alt):
    if not alt:
        cargo_hold_str = [
            "=============Cargo Hold=================",
            "",
            "",
            "",
            "",
            " _____",
            "(_____)   ______           _______",
            "|     |  |______|         /___o___\ ",
            "|     |  |______|        | chest   |",
            "|     |  |______|        |_________|    ",
            "========================================",
        ]
    else:
        cargo_hold_str = [
            "=============Cargo Hold=================",
            "",
            "",
            "",
            "",
            " _____                     _______",
            "(_____)   ______          /       \ ",
            "|     |  |______|        |=========| ",
            "|     |  |______|        | chest   |",
            "|     |  |______|        |_________|    ",
            "========================================",
        ]

    for s in cargo_hold_str:
        print s


def ship_wheel():
    ship_wheel_str = [
            "           / ///         \\\\\\ \ ",
            "          /\///   _____   \\\\\\/\ ",
            "         /\///  /\  |  /\  \\\\\\/\ ",
            "        / ///  /  \ | /  \  \\\\\\ \ ",
            "       /\///  |-----0-----|  \\\\\\/\ ",
            "      /\///    \  / | \  /    \\\\\\/\ ",
            "     / ///      \/__|__\/      \\\\\\ \ ",
            "    /\///         |   |         \\\\\\/\ ",
            "   /\///          |   |          \\\\\\/\ ",
            "  / ///           |   |           \\\\\\ \ ",
            "  \///           /     \           \\\\\\/ ",
            "======================================"
        ]

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def map1(gamestate, mechanics):
    map1_figure = mechanics["Map1_Figure"]
    print "[=================================================]"
    for x in range(0, MAP_WIDTH):
        print "|",
        for y in range(0, MAP_HEIGHT):
            # TODO
            # if i, j == player pos then print " X "
            if gamestate.characterPos[0] == x and gamestate.characterPos[1] == y:
                print " X ",
                continue
            if gamestate.isGorillaAngry and GORILLA_POS["x"] == x and GORILLA_POS["y"] == y:
                print " G ",
                continue
            # if i, j == native pos then print " N "
            # if i, j == native chief pos then print "NC "
            print map1_figure[x][y],
        print "|"
    print "[=================================================]"


def map2(gamestate, mechanics):
    map2_figure = mechanics["Map2_Figure"]
    print "[=================================================]"
    for x in range(0, MAP_WIDTH):
        print "|",
        for y in range(0, MAP_HEIGHT):
            # TODO
            # if i, j == player pos then print " X "
            print map1_figure[x][y],
        print "|"
    print "[=================================================]",
