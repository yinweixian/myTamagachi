class Human(object):

    def __init__(self,name,hairColor,eyeColor,height,weight,iq,gender,race,changeDirection):
        self.hairColor=hairColor
        self.eyeColor=eyeColor
        self.height=height
        self.weight=weight
        self.iq=iq
        self.gender=gender
        self.race=race
        self.name=name
        self.changeDirection=changeDirection
    def introduceSelf(self):
        print("hello my name is ",self.name)
    def discribeSelf(self):
        print("I have",self.hairColor,"hair")
        print("I have",self.eyeColor,"eyes")
        print("I am",self.height,"feet tall")
        print("I am",self.weight,"lb")
        print("my iq is a",self.iq)
        print("I identify as a(n)",self.gender)
        print("I am of the",self.race,"race")
    def turn(self,changeDirection):
        direction = "north"
        if changeDirection =="left":
            direction = "west"
        elif changeDirection =="right":
            direction = "east"
        else:
            direction = "north"
        print(direction)
    def bmi_calc(self):
        height = int(input("enter your height in feet"))
        weight = int(input("enter your weight in pounds"))
        inch = int(input("enter inches to add to your height"))
        height = height*12
        height = height+inch
        bmi = weight*703
        height = height*height
        bmi = bmi/height
        print(bmi)
        if bmi<18:
            print("you are underweight")
        elif bmi<24 and bmi>18:
            print("you are a healthy weight")
        elif bmi>25:
            print("you are overweight")




thrain = Human("thrain","blond","grey",4,184,70,"male","dwarven","")
thrain.introduceSelf()
thrain.discribeSelf()
thrain.turn(input("enter a direction"))
thrain.bmi_calc()
print("\n\n")
ulag = Human("ulag","black","black",7,230,63,"male","orcish","")
ulag.introduceSelf()
ulag.discribeSelf()
ulag.turn(input())
ulag.bmi_calc()
print("\n\n")
lunalias = Human("lunalias","silver","bright blue",6,195,87,"female","elvish","")
lunalias.introduceSelf()
lunalias.discribeSelf()
lunalias.turn(input())
lunalias.bmi_calc()
