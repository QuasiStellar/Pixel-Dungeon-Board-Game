

types = {"Minion": 0, "Seed": 1, "Potion": 2, "Scroll": 3, "Artifact": 4,
         "Elite": 5, "Boss": 6, "Wand": 7, "Ally": 8, "Ranged": 9, "Unique": 10}
chapters = {0: "sewers", 1: "prison", 2: "caves", 3: "metropolis", 4: "demon_halls"}


class Card:

    def __init__(self, name, power, description, card_type, is_enemy, chapter):
        self.name = name
        self.power = power
        self.description = description
        self.card_type = card_type
        self.is_enemy = is_enemy
        self.chapter = chapter
