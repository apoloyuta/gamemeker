from random import choice

def generate_quest(player):
    quests = [
        "隠された宝を見つけよ",
        "魔獣を討伐せよ",
        "村人の依頼を遂行せよ",
        "古代遺跡の謎を解け"
    ]
    return choice(quests)
