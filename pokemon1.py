"""
This program prints out the names of two Pokémon
Author: Adejumo Toluwani
When: Wednesday, 5th April, 2023.
"""


class Pokemon:
    """
    This is the Pokémon class which defines the properties and methods of a Pokémon.
    """
    def __init__(self, name, attack, defense, max_health, current_health):
        """
        Initializes a new Pokémon instance with the given name, attack, defense, maximum health, and current health.
        """
        self.name = name
        self.attack = attack
        self.defense = defense
        self.max_health = max_health
        self.current_health = current_health


def main():
    """
    Battle of two Pokémon
    """
    pokemon1 = Pokemon("Pikachu", 55, 40, 35, 35)
    pokemon2 = Pokemon("Bulbasaur", 49, 49, 45, 45)
    print(f"Welcome, {pokemon1.name} and {pokemon2.name}!")


if __name__ == '__main__':
    main()
