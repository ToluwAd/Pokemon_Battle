"""
This program randomly selects two Pokémon to battle
Author: Adejumo Toluwani
When: Thursday, 6th April, 2023.
"""

import random


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

    def __str__(self):
        """
        Return a string representation of the Pokémon.
        """
        return f"{self.name} (health: {self.current_health}/{self.max_health})"

    def lose_health(self, amount: int):
        """
        Lose health from the Pokémon.
        """
        if amount > 0:
            self.current_health -= amount
            if self.current_health < 0:
                self.current_health = 0.

    def is_alive(self):
        """
        Return True if the Pokémon has health remaining.
        """
        return self.current_health > 0

    def revive(self):
        """
        Revive the Pokémon.
        """
        self.current_health = self.max_health


def read_pokemon_from_file(filename: str):
    """
    Read a list of Pokémon from a file.
    """
    pokemon_list = []
    with open(filename, "r", encoding="utf-8") as f:
        f.readline()
        for line in f:
            values = line.strip().split("|")
            name = values[0]
            attack = int(values[1])
            defense = int(values[2])
            max_health = int(values[3])
            current_health = int(values[3])
            pokemon_list.append(Pokemon(name, attack, defense, max_health, current_health))
        return pokemon_list


def main():
    """
    Battle of two random Pokémon.
    """
    pokemon_list = read_pokemon_from_file("all_pokemon.txt")
    pokemon1 = random.choice(pokemon_list)
    pokemon2 = random.choice(pokemon_list)
    while pokemon1 == pokemon2:
        pokemon2 = random.choice(pokemon_list)
    print(f"Welcome, {pokemon1} and {pokemon2}!")


if __name__ == "__main__":
    main()
