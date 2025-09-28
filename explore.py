from random import choice

locations = ["森", "洞窟", "湖", "塔", "遺跡"]

def move(player):
    player.location = choice(locations)
    return f"{player.name}は{player.location}へ移動した"
