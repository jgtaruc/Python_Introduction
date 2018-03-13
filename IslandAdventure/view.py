def welcome():
    return

def main_menu(gamestate):
    return


def inventory(gamestate):
    return


def objectives(gamestate):
    return


def tile_information(gamestate):
    return


def intro(gamestate):
    return


def map1(gamestate):
    map1_figure = gamestate.initialValues["Map1_Figure"]
    print "[=================================================]"
    for x in range(0, MAP_WIDTH):
        print "|",
        for y in range(0, MAP_HEIGHT):
            # TODO
            # if i, j == player pos then print " X "
            if gamestate.characterPos[0] == x and gamestate.characterPos[1] == y:
                map1_figure[x][y] = " X "
            # if i, j == native pos then print " N "
            # if i, j == native chief pos then print "NC "
            print map1_figure[x][y],
        print "|"
    print "[=================================================]",


def map2(gamestate):
    map2_figure = gamestate.initialValues["Map2_Figure"]
    print "[=================================================]"
    for x in range(0, MAP_WIDTH):
        print "|",
        for y in range(0, MAP_HEIGHT):
            # TODO
            # if i, j == player pos then print " X "
            print map1_figure[x][y],
        print "|"
    print "[=================================================]",
