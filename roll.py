import random
while 1==1:
    class Roll:
        def __init__(self,sides):
            self.sides = sides
        def comin(self):
            print("You rolled a: ")
            y = random.randint(1, int(self.sides) + 1)
            print(y)
    roll = Roll(input("What number of sides do you need? "))
    roll.comin()
    print(input("press ENTER to roll again!"))


