class Camel (Animal):
    def __init__(self):
        self.noise = "What the heelllllll"
        self.angry = "You're banned"
    def makeNoies (self, isHungry):
        if isHungry:
            print("You got koolaid")
        else:
            super().makeNoise()
    def angry (self, isangry):
        if isangry:
            print("So.. you're banned")
        else:
            print ("Thats the method")