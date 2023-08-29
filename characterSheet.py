import os
import json
import roll

class NewCharacter:
    def __init__(self):
        self.name = input("What is your character's name? ")

        # Check if character file already exists
        if os.path.isfile(f"{self.name}.json"):
            # Load character data from file
            with open(f"{self.name}.json", "r") as f:
                self.data = json.load(f)
        else:
            # Create a new character
            self.race = input("What race would you like to pick?")
            self.characterClass = input("Great choice. What class are they going to be?")
            self.age = input(f"How old is your character, {self.name}? ")
            self.height = input(f"How tall is your character, {self.name}? ")
            self.weight = input(f"How much does your character weigh?")
            self.strength = roll.roll(20)
            self.dexterity = roll.roll(20)
            self.constitution = roll.roll(20)
            self.intelligence = roll.roll(20)
            self.wisdom = roll.roll(20)
            self.charisma = roll.roll(20)

            # Store character data in a dictionary
            self.data = {
                'race': self.race,
                'class': self.characterClass,
                'name': self.name,
                'age': self.age,
                'height': self.height,
                'weight': self.weight,
                'strength': self.strength,
                'dexterity': self.dexterity,
                'constitution': self.constitution,
                'intelligence': self.intelligence,
                'wisdom': self.wisdom,
                'charisma': self.charisma,
            }

            # Save character data to a file
            with open(f"{self.name}.json", "w") as f:
                json.dump(self.data, f)


# Create a new character or load existing character
character = NewCharacter()

# Print the character's name and data
print(f"Character loaded: {character.name}")
print(character.data)
    
