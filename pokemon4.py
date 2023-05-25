"""
This program will implement the actual battle between the Pokémon
Author: Adejumo Toluwani
When: Thursday, 6th April, 2023
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

    def attempt_attack(self, other: "Pokemon"):
        """
        This program returns damage caused and luck 
        """        
        luck = round(random.uniform(0.7, 1.3), 1)  # Calculate luck coefficient
        damage = round(self.attack * luck)  # Calculate damage

        return luck, damage


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
    pokemon_list = read_pokemon_from_file("all_pokemon.txt")
    print("Welcome to the Pokémon Battle Game!")
    print("Selecting two random Pokémon...")

    # Randomly select two Pokémon from the list
    pokemon1 = random.choice(pokemon_list)
    pokemon2 = random.choice(pokemon_list)
    luck, damage = Pokemon.attempt_attack(pokemon1, pokemon2)

    print(f"Welcome, {pokemon1.name} (health: {pokemon1.current_health}/{pokemon1.max_health}) and {pokemon2.name} "
          f"(health: {pokemon2.current_health}/{pokemon2.max_health})!")
    print("Let the battle begin!")

    # Battle for a maximum of 10 rounds
    for i in range(1, 11):
        print(f"\nRound {i} begins! {pokemon1.name} (health: {pokemon1.current_health}/{pokemon1.max_health}) and "
              f"{pokemon2.name} (health: {pokemon2.current_health}/{pokemon2.max_health})")

        # Pokemon 1 attacks Pokemon 2
        if damage > pokemon2.defense:
            health_loss = damage - pokemon2.defense
            pokemon2.lose_health(health_loss)
            print(f"{pokemon1.name} attacks {pokemon2.name} for {health_loss} damage!")
            print("Attack is successful!")

            if not pokemon2.is_alive():
                print(f"{pokemon2.name} has 0 health remaining!")

                if random.random() < 0.5:
                    pokemon2.revive()
                    print(f"{pokemon2.name} has been revived!")
                else:
                    print(f"{pokemon2.name} is dead!")

                # Pokémon 1 wins
                print(
                    f"\n{pokemon1.name} (health: {pokemon1.current_health}/{pokemon1.max_health}) has won in {i} rounds!")
                return

            else:
                print(f"{pokemon2.name} has {pokemon2.current_health} health remaining!")

        else:
            print(f"{pokemon1.name}'s attack is blocked by {pokemon2.name}'s defense!")

        # Pokemon 2 attacks Pokemon 1
        if damage > pokemon1.defense:
            health_loss = damage - pokemon1.defense
            pokemon1.lose_health(health_loss)
            print(f"{pokemon2.name} attacks {pokemon1.name} for {health_loss} damage!")
            print("Attack is successful!")

            if not pokemon1.is_alive():
                print(f"{pokemon1.name} has 0 health remaining!")

                if random.random() < 0.5:
                    pokemon1.revive()
                    print(f"{pokemon1.name} has been revived!")
                else:
                    print(f"{pokemon1.name} is dead!")

                # Pokémon 2 wins
                print(
                    f"\n{pokemon2.name} (health: {pokemon2.current_health}/{pokemon2.max_health}) has won in {i} rounds!")
                return

            else:
                print(f"{pokemon1.name} has {pokemon1.current_health} health remaining!")

        else:
            print(f"{pokemon2.name}'s attack is blocked by {pokemon1.name}'s defense!")

    else:
        # It's a tie
        print("It's a tie")


if __name__ == "__main__":
    main()
