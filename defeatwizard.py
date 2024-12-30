import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power, heal_strength,):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.heal_strength = heal_strength
        self.max_health = health  
        
    def attack(self, opponent):
        damage = random.randint(0, self.attack_power)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    def heal(self):
        if self.health + self.max_health < self.max_health:
            self.health += self.heal_strength
            print(f"{self.name} has healed {self.heal_strength} points of health. Current health: {self.health}")
        elif self.health >= self.max_health:
            print(f"Health cannot exceed max for your character. Current health: {self.health}")  
        

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25, heal_strength=14)

    def special_attack(self, opponent):
        print("Choose which special ability you want to use.")
        print("1. Furious Strike (Deals extra damage)")
        print("2. Warriors Grace (Evades the wizards next attack)") 
        
        special_choice = input("Enter your choice of special ability:")
        if special_choice == "1":
            opponent.health -= 40
            print(f"{self.name} attacks {opponent.name} for 40 damage.")
        elif special_choice == "2":
            self.health += 15
            print("You have dodged the wizards attack. Prepare for your next move.")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35, heal_strength=20)
        
    def special_attack(self, opponent):
        print("Choose which special ability you want to use.")
        print("1. Massive Fire Ball (Deals extra damage)")
        print("2. Impenetrable Ward (Evades the wizards next attack)") 
        
        special_choice = input("Enter your choice of special ability:")
        if special_choice == "1":
            opponent.health -= 50
            print(f"{self.name} attacks {opponent.name} for 50 damage.")
        elif special_choice == "2":
            self.health += 15
            print("You have dodged the wizards attack. Prepare for your next move.") 

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15, heal_strength=0)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Create Archer class
class ElvinArcher(Character):
    def __init__(self, name,):
        super().__init__(name, health=120, attack_power=30, heal_strength=16)
        
    def special_attack(self, opponent):
        print("Choose which special ability you want to use.")
        print("1. Double Shot (Deals extra damage)")
        print("2. Elegant Elvin Glide (Evades the wizards next attack)") 
        
        special_choice = input("Enter your choice of special ability:")
        if special_choice == "1":
            opponent.health -= 45
            print(f"{self.name} attacks {opponent.name} for 45 damage.")
        elif special_choice == "2":
            self.health += 15
            print("You have dodged the wizards attack. Prepare for your next move.")
    
# Create Dwarf class 
class Dwarf(Character):
    def __init__(self, name):
        super().__init__(name, health=145, attack_power=20, heal_strength=12)
        
    def special_attack(self, opponent):
        print("Choose which special ability you want to use.")
        print("1. Heavy Handed Chop (Deals double damage)")
        print("2. Dwarf Barrel Roll (Evades the wizards next attack)") 
        
        special_choice = input("Enter your choice of special ability:")
        if special_choice == "1":
            opponent.health -= 40
            print(f"{self.name} attacks {opponent.name} for 40 damage.")
        elif special_choice == "2":
            self.health += 15
            print("You have dodged the wizards attack. Prepare for your next move.")
    
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Elvin Archer") 
    print("4. Dwarf")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return ElvinArcher(name)
    elif class_choice == '4':
        return Dwarf(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_attack(wizard)
            
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
            return battle(player, wizard)
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()