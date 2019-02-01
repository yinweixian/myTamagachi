import sys

class mytamagachi(object):
    """a virtual pet creator class"""
    def __init__(self,name):
        """assigning all the variables"""
        self.name = name
        self.hunger = 0
        self.boredem = 0
        self.age = 0

    def __pass_time(self,hunger,boredem,age):
        """increasing boredem hunger and age"""
        boredem += 1
        hunger += 1
        age += 1

    def play(self,boredem):
        print("Hello human. Lets play now!")
        print('"you play with your tamagachi"')
        print("That was fun lets do it again sometime!")
        boredem = boredem - 15
        if boredem < 0:
            boredem = 0
        self.__pass_time(self.hunger,self.boredem,self.age)



    def talk(self,name):
        print("hello there. my name is",name)
        print("idk what this thing is supposed to say")
        self.__pass_time(self.hunger,self.boredem,self.age)

    def eat(self,hunger):
        print("lets have some food!!")
        print('"you watch as your tamagachi munches some food"')
        print("Im done now!")
        hunger = hunger - 15
        self.__pass_time(self.hunger,self.boredem,self.age)

    @property
    def mood(self,boredem,hunger):
        """calculates the unhappiness and tells you how unhappy it is it returns the mood"""
        unhappiness = self.hunger +self.boredem
        if unhappiness < 5:
            m = "happy"
        elif 5<+unhappiness<=10:
            m = "okay"
        elif 11 <=unhappiness<=15:
            m = "frustrated"
        else:
            m = "mad"
        return m





def main():
    yours = mytamagachi(input("enter a name for your tamagachi"))

    choice = 2
    while choice != 0:
        choice = int(input("press 1 for your critter to talk\npress 2 to feed your critter\npress "
                           "3 to play with your critter.\nyou may exit by pressing 0"))
        if choice == 1:
            yours.talk(yours)
        if choice == 2:
            yours.eat(yours)
        if choice == 3:
            yours.play(yours)

main()