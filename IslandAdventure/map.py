import models, json

MAP_WIDTH = 12
MAP_HEIGHT = 12
MAP = [[0 for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)] 

class Tile:
    def __init__(self, kind, x, y, obj, canGO, description, description_short, reached):
        self.kind = kind
        self.posx = x
        self.posy = y
        self.object = obj
        self.canGo = canGO
        self.description_long = description
        self.description_short = description_short
        self.reached = reached

    def location(self):
        return (self.posx, self.posy)

    def description(self):
        if self.__reached:
            return self.description_short
        else:
            return self.description_long

# for x in range(MAP_WIDTH):
#     for y in range(MAP_HEIGHT):
#         MAP[x][y] = (Tile("empty", x, y, None, True, "Empty tile", "Empty", False))

data = json.load(open("gameMechanics.json"))
print data["Tiles"]["Galley"]["kind"]