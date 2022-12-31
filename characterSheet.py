import roll
import dictionary
class NewCharacter:
    def __init__(self):
        self.race = input("What race would you like to pick?")
        self.characterClass = input("Great choice. What class are they going to be?")
        self.name = input("Every great hero needs a name. What is yours? ")
        self.age = input(f"How old are you, {self.name}? ")
        self.height = input(f"Tell me how tall you are {self.name}. ")
        self.weight = input(f"How much do you weight if you don't mind me asking?")
        self.strength = roll(20)
        self.dexterity = roll(20)
        self.constitution = roll(20)
        self.intelligence = roll(20)
        self.wisdom = roll(20)
        self.charisma = roll(20)
NewCharacter()

    
