class Hero:
    """Base class shared by all academy heroes."""

    def __init__(self, name, energy, power):
        self.name = name
        self.energy = energy
        self.power = power

    def status(self):
        return f"{self.name} | Energy: {self.energy} | Power: {self.power}"

    def attack(self, opponent):
        """Default attack; subclasses may override this."""
        damage = self.power
        opponent.take_damage(damage)
        self.energy = max(0, self.energy - 5)
        print(f"{self.name} uses a basic attack on {opponent.name} for {damage} damage.")

    def take_damage(self, damage):
        self.energy = max(0, self.energy - damage)
        print(f"{self.name} takes {damage} damage. Energy is now {self.energy}.")

    def is_active(self):
        return self.energy > 0


class FireHero(Hero):
    def attack(self, opponent):
        damage = self.power + 15
        opponent.take_damage(damage)
        self.energy = max(0, self.energy - 10)
        print(f"{self.name} unleashes Flame Burst on {opponent.name} for {damage} damage.")


class TechHero(Hero):
    def attack(self, opponent):
        damage = self.power + 10
        opponent.take_damage(damage)
        self.energy = max(0, self.energy - 7)
        print(f"{self.name} launches a Tech Blast on {opponent.name} for {damage} damage.")


def battle(hero_one, hero_two):
    """Alternate attacks until one hero runs out of energy."""
    print(f"\nBattle: {hero_one.name} vs {hero_two.name}")
    turn = 0

    while hero_one.is_active() and hero_two.is_active():
        attacker = hero_one if turn % 2 == 0 else hero_two
        defender = hero_two if turn % 2 == 0 else hero_one

        attacker.attack(defender)
        turn += 1

    if hero_one.is_active():
        winner = hero_one
    elif hero_two.is_active():
        winner = hero_two
    else:
        winner = None

    if winner:
        print(f"Winner: {winner.name}")
    else:
        print("The battle ends in a draw.")

    return winner


if __name__ == "__main__":
    blaze = FireHero("Blaze", energy=100, power=20)
    circuit = TechHero("Circuit", energy=100, power=18)

    print("Superhero Academy Simulator")
    print(blaze.status())
    print(circuit.status())
    battle(blaze, circuit)

    print("\nFinal status:")
    print(blaze.status())
    print(circuit.status())
