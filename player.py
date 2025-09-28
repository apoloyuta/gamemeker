class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.level = 1
        self.experience = 0
        self.inventory = []
        self.location = "村"
        self.skills = []

    def level_up(self):
        required_exp = self.level * 50
        if self.experience >= required_exp:
            self.level += 1
            self.hp = 100
            self.experience -= required_exp
            return True
        return False
