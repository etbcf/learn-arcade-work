class Star:

    def __init__(self):
        print("A star is born!")


new_event = Star()


class Monster:

    def __init__(self, health, name):
        self.health = health
        self.name = name


monster = Monster(75, "Gooba")
print("Health:", monster.health, "Name:", monster.name)
