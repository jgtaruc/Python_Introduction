
class GameObject():
    def __init__(self, itemtype, integrity, description):
        self.__type = itemtype
        self.__integrity = integrity
        self.description = description

    def kind(self):
        return self.__type

    def loseIntegrity(self):
        if not self.__integrity > 0:
            return False
        self.__integrity -= 1
        return True

    def integrity(self):
        return self.__integrity


class Item(GameObject):
    def __init__(self, itemtype, integrity, description, name):
        GameObject.__init__(self, itemtype, integrity, description)
        self.__name = name

    def name(self):
        return self.__name


class Inventory():
    def __init__(self, limit, items=None):
        if items is not None:
            self.__list = items
        else:
            self.__limit = limit
            self.__list = []

    def add(self, item):
        if(len(self.__list) >= self.__limit):
            return False
        self.__list.append(item)
        return True

    def drop(self, index):
        if len(self.__list) == 0:
            return False

        if index > len(self.__list)-1:
            return False

        item = self.__list[index]
        self.__list.remove(item)
        del item
        return True

    def showItems(self):
        return self.__list


class Character(GameObject):
    def __init__(self, itemtype, integrity, description, inventory_limit, name, items=None):
        GameObject.__init__(self, itemtype, integrity, description)
        self.__name = name
        self.__inventory = Inventory(inventory_limit, items)

    def name(self):
        return self.__name

    def pickItem(self, item):
        return self.__inventory.add(item)

    def dropItem(self, index):
        return self.__inventory.drop(index)

    def inventory(self):
        return self.__inventory.showItems()


class Gorilla(GameObject):
    def __init__(self, itemtype, integrity, description, name, dialog, alt_dialog):
        GameObject.__init__(self, itemtype, integrity, description)
        self.__name = name
        self.dialog = dialog
        self.alt_dialog = alt_dialog
        self.isGrumpy = True

    def name(self):
        return self.__name

    def talk(self):
        if self.isGrumpy:
            return self.dialog
        else:
            return self.alt_dialog


class Parrot(GameObject):
    def __init__(self, itemtype, integrity, description, name, known_words, dialog, alt_dialog):
        GameObject.__init__(self, itemtype, integrity, description)
        self.__name = name
        self.__known_words = known_words
        self.__dialog = dialog
        self.__alt_dialog = alt_dialog

    def name(self):
        return self.__name

    def talk(self, sound):
        sound = sound.lower()
        words = sound.split(" ")
        return self.respond(words)

    def respond(self, words):
        condMet = False
       
        for w in words:
            if w in self.__known_words:
                condMet = True
                break

        if condMet:
            return self.__alt_dialog
        else:
            res = ""
            for i, s in enumerate(words):
                res += self.__dialog[i%len(self.__dialog)]
            return res + "?"


class Prisoner(GameObject):
    def __init__(self, itemtype, integrity, description, name, dialog, alt_dialog):
        GameObject.__init__(self, itemtype, integrity, description)
        self.__name = name
        self.dialog = dialog
        self.alt_dialog = alt_dialog
        self.imprisoned = True

    def name(self):
        return self.__name

    def talk(self):
        if self.imprisoned:
            return self.dialog
        else:
            return self.alt_dialog


class Native(GameObject):
    def __init__(self, itemtype, integrity, description, name, position, dialog, item=None):
        GameObject.__init__(self, itemtype, integrity, description)
        self.__name = name
        self.__position = position
        self.dialog = dialog
        self.item = item
    
    def name(self):
        return self.__name

    def position(self):
        return self.__position

    def talk(self):
        return self.dialog


class Tile:
    def __init__(self, kind, x, y, objs, canGO, description, description_short, asset=None):
        self.id = str(x)+str(y)
        self.kind = kind
        self.posx = x
        self.posy = y
        self.object = objs
        self.canGo = canGO
        self.description_long = description
        self.description_short = description_short
        if asset is not None:
            self.asset = asset

    def location(self):
        return (self.posx, self.posy)

    def description(self):
        if self.__reached:
            return self.description_short
        else:
            return self.description_long