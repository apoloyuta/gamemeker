class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

def gain_item(player):
    items = [
        Item("炎の剣", "攻撃力+10"),
        Item("回復薬", "HP+30"),
        Item("魔法の盾", "防御力+5")
    ]
    item = choice(items)
    player.inventory.append(item)
    return item
