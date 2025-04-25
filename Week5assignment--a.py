# Assignment 1

class Superhero:
    def __init__(self, name, powers, weakness):
        self.name = name
        self.powers = powers
        self.weakness = weakness

    def display_superhero(self):
        print(f"Superhero: {self.name}\nPowers: {self.powers}\nWeakness: {self.weakness}")

    def use_power(self, power):
        if power in self.powers:
            print(f"{self.name} uses their {power} power!")
        else:
            print(f"{self.name} does not possess the {power} power.")

    def react_to_weakness(self):
        print(f"{self.name} reacts to their weakness, struggling to fight on!")

# Example of creating a Superhero object
spiderman = Superhero("Spiderman", ["webs", "spider-sense"], "radiation exposure")
spiderman.display_superhero()
spiderman.use_power("webs")
spiderman.react_to_weakness()

# Inheritance Layer for the hero

class Hero(Superhero):
    def __init__(self, name, powers, weakness, secret_identity):
        super().__init__(name, powers, weakness)
        self.secret_identity = secret_identity

    def reveal_identity(self):
        print(f"{self.name} is actually {self.secret_identity}!")


ironman = Hero("Ironman", ["repulsor blast", "iron suit"], "magnetism", "Tony Stark")
ironman.reveal_identity()