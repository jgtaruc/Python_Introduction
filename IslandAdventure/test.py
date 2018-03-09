import models, json

data = json.load(open("gameMechanics.json"))

items = data["Items"]

def unit_test_item():
    obj = items["Knife"]
    itm = models.Item(obj["type"], obj["integrity"], obj["description"], obj["name"])
    assert itm.kind() == obj["type"]
    assert itm.name() == obj["name"]
    assert itm.loseIntegrity() == True
    assert itm.integrity() == obj["integrity"] - 1
    assert itm.loseIntegrity() == True
    assert itm.loseIntegrity() == True
    assert itm.loseIntegrity() == False
    assert itm.loseIntegrity() == 0
    assert itm.description == obj["description"]
    
    obj = items["Key"]
    itm = models.Item(obj["type"], obj["integrity"], obj["description"], obj["name"])
    assert itm.kind() == obj["type"]
    assert itm.name() == obj["name"]
    assert itm.loseIntegrity() == True
    assert itm.integrity() == obj["integrity"] - 1
    assert itm.loseIntegrity() == True
    assert itm.loseIntegrity() == True
    assert itm.integrity() == 9996
    assert itm.description == obj["description"]    

    obj = items["Banana"]
    itm = models.Item(obj["type"], obj["integrity"], obj["description"], obj["name"])
    assert itm.kind() == obj["type"]
    assert itm.name() == obj["name"]
    assert itm.loseIntegrity() == True
    assert itm.integrity() == obj["integrity"] - 1
    assert itm.loseIntegrity() == False
    assert itm.description == obj["description"]
    
    obj = items["Treasure"]
    itm = models.Item(obj["type"], obj["integrity"], obj["description"], obj["name"])
    assert itm.kind() == obj["type"]
    assert itm.name() == obj["name"]
    assert itm.loseIntegrity() == True
    assert itm.integrity() == obj["integrity"] - 1
    assert itm.description == obj["description"]


def unit_test_inventory():
    inventory = models.Inventory(3, ["a", "b"])
    assert inventory.showItems() == ["a", "b"]
    assert inventory.drop(0) == True
    assert inventory.showItems() == ["b"]
    assert inventory.drop(1) == False
    assert inventory.drop(0) == True
    assert inventory.showItems() == []

    inventory = models.Inventory(3)
    assert inventory.drop(0) == False
    assert inventory.add("a") == True
    assert inventory.add("b") == True
    assert inventory.showItems() == ["a", "b"]
    assert inventory.add("c") == True
    assert inventory.add("d") == False


def unit_test_character():
    obj = data["Character"]
    c = models.Character(obj["type"], obj["integrity"], obj["description"], obj["inventory_limit"], "character name")
    assert c.name() == "character name"
    assert c.pickItem("a") == True
    assert c.pickItem("b") == True
    assert c.inventory() == ["a", "b"]
    assert c.pickItem("c") == True
    assert c.pickItem("d") == False
    assert c.dropItem(1) == True
    assert c.inventory() == ["a", "c"]
    assert c.kind() == obj["type"]
    assert c.loseIntegrity() == True
    assert c.integrity() == obj["integrity"]-1
    assert c.description == obj["description"]


def unit_test_gorilla():
    obj = data["Gorilla"]
    g = models.Gorilla(obj["type"], obj["integrity"], obj["description"], obj["name"], obj["dialog"], obj["alt_dialog"])
    assert g.name() == obj["name"]
    assert g.integrity() == obj["integrity"]
    assert g.kind() == obj["type"]
    assert g.description == obj["description"]
    assert g.loseIntegrity() == True
    assert g.integrity() == obj["integrity"]-1
    assert g.isGrumpy == True
    assert g.talk() == obj["dialog"]
    g.isGrumpy = False
    assert g.talk() == obj["alt_dialog"]


def unit_test_parrot():
    obj = data["Parrot"]
    p = models.Parrot(obj["type"], obj["integrity"], obj["description"], obj["name"], obj["known_words"], obj["dialog"], obj["alt_dialog"])
    assert p.name() == obj["name"]
    assert p.integrity() == obj["integrity"]
    assert p.kind() == obj["type"]
    assert p.description == obj["description"]
    assert p.loseIntegrity() == True
    assert p.integrity() == obj["integrity"]-1
    assert p.talk("Hi how are you?") == "lorem ipsum dolor sit?"
    assert p.talk("Hello") == obj["alt_dialog"]


def unit_test_prisoner():
    obj = data["Prisoner"]
    p = models.Prisoner(obj["type"], obj["integrity"], obj["description"], obj["name"], obj["dialog"], obj["alt_dialog"])
    assert p.name() == obj["name"]
    assert p.integrity() == obj["integrity"]
    assert p.kind() == obj["type"]
    assert p.description == obj["description"]
    assert p.loseIntegrity() == True
    assert p.integrity() == obj["integrity"]-1
    assert p.imprisoned == True
    assert p.talk() == obj["dialog"]
    p.imprisoned = False
    assert p.talk() == obj["alt_dialog"]


def unit_test_native():
    obj = data["Native_Chief"]
    nc = models.Native(obj["type"], obj["integrity"], obj["description"], obj["name"], obj["position"], obj["dialog"], obj["item"])
    assert nc.name() == obj["name"]
    assert nc.integrity() == obj["integrity"]
    assert nc.kind() == obj["type"]
    assert nc.description == obj["description"]
    assert nc.loseIntegrity() == True
    assert nc.integrity() == obj["integrity"]-1
    assert nc.position() == obj["position"]
    assert nc.talk() == obj["dialog"]

    obj = data["Native"]
    ng = models.Native(obj["type"], obj["integrity"], obj["description"], obj["name"], obj["position"], obj["dialog"])
    assert ng.name() == obj["name"]
    assert ng.integrity() == obj["integrity"]
    assert ng.kind() == obj["type"]
    assert ng.description == obj["description"]
    assert ng.loseIntegrity() == True
    assert ng.integrity() == obj["integrity"]-1
    assert ng.position() == obj["position"]
    assert ng.talk() == obj["dialog"]


unit_test_item()
unit_test_inventory()
unit_test_character()
unit_test_gorilla()
unit_test_parrot()
unit_test_prisoner()
unit_test_native()