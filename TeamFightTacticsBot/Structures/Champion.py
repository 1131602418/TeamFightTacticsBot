class Champion:
    def __init__(self, name, cost, health, attack_speed, attack_damage, attack_range, armor, magic_resist, synergies):
        self.name = name
        self.cost = cost
        self.health = health
        self.attack_speed = attack_speed
        self.attack_damage = attack_damage
        self.attack_range = attack_range
        self.armor = armor
        self.magic_resist = magic_resist
        self.synergies = synergies
        self.level = 1

    def __str__(self):
        string = "[" + \
               "Champion: " + self.name + \
               ", level: " + str(self.level) + \
               ", Cost: " + str(self.cost) + \
               ", Health: " + str(self.health) + \
               ", Attack Speed: " + str(self.attack_speed) + \
               ", Attack Damage: " + str(self.attack_damage) + \
               ", Attack Range: " + str(self.attack_range) + \
               ", Armor: " + str(self.armor) + \
               ", Magic Resist: " + str(self.magic_resist)
        for synergy in self.synergies:
            string = string + ", Synergy: " + str(synergy.value)
        string += "]"
        return string

    def __eq__(self, other):
        return self.name == other.name and self.level == other.level

    def is_ranged(self):
        return self.attack_range != 1
