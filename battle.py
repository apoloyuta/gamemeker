from random import randint

class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

def fight(player, enemy):
    damage = randint(5, 15) + player.level * 2
    enemy.hp -= damage
    enemy_attack = randint(5, 10) + enemy.attack
    player.hp -= enemy_attack
    return f"{player.name}は{enemy.name}に{damage}ダメージ！ {enemy.name}の反撃でHP-{enemy_attack}"
