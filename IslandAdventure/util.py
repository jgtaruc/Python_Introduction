import models

MAP_WIDTH = 12
MAP_HEIGHT = 12

def generate_map1(outline):
    tile_kinds = data["Tiles"]
    positions = data["Positions"]
    game_map = outline

    def getCoordInfo(x, y):
        if positions["Banana"]["x"] == x and positions["Banana"]["y"] == y:
            return tile_kinds["Banana_Tree"]
        elif positions["CaptnQtr"]["x"] == x and positions["CaptnQtr"]["y"] == y:
            return tile_kinds["Captain_Quarters"]
        elif positions["LadderUD"]["x"] == x and positions["LadderUD"]["y"] == y:
            return tile_kinds["Top_Deck_Ladder"]
        elif positions["Wheel"]["x"] == x and positions["Wheel"]["y"] == y:
            return tile_kinds["Ship_Wheel"]
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


def generate_map2(outline):
    tile_kinds = data["Tiles"]
    positions = data["Positions"]
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


def fill_map1(gamestate):
    # TODO
    return


def fill_map2(gamestate):
    # TODO
    return