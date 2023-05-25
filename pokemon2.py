"""
This program calls the string representation of the object
Author: Adejumo Toluwani
When: Thursday, 6th April, 2023.
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

    def __str__(self):
        """
        Return a string representation of the Pokémon.
        """
        return f"{self.name} (health: {self.current_health}/{self.max_health})"

    def lose_health(self, amount: int) -> None:
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


def main():
    """
    Battle of two Pokémon
    """
    pokemon1 = Pokemon("Pikachu", 55, 40, 35, 35)
    pokemon2 = Pokemon("Bulbasaur", 49, 49, 45, 45)
    print(f"Welcome, {pokemon1} and {pokemon2}!")


if __name__ == '__main__':
    main()
