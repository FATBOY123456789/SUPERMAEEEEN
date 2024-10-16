class Bird:
    def __init__(self,type,colour):
        self.type=type
        self.colour=colour
    def whatitdoes(self):
        print('It can walk on lands and cant fly but produce cute babies of their own species :)')
    def display(self):
        print('It is a/an ',self.type,'its colour is ',self.colour)
class Birdietypie(Bird):
    def __init__(self, type, colour,age):
        super().__init__(type, colour)
        self.age=age
    def whatitdoes(self):
         super().whatitdoes()
    def display(self):
        return super().display()
pengu=Birdietypie('Penguin','Light_Blue','6 months')
pengu.whatitdoes()
print('This little guy is a/an',pengu.type,'It is a shade of blue, ',pengu.colour,'!, it is just ',pengu.age,'old.')