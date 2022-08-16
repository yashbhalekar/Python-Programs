
class Person():

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self):
        print(self.name +" "+"is speaking so true")

    def works(self):
        print(self.name +" "+ "works in a product company")

    def years(self):
        print(self.name +" "+"is"+" "+self.age+" "+ "year's old.")

t = Person("Tom" , "25")
t.speak()
t.works()
t.years()

" " " MULTIPLE INSTANCES " " "

d= Person("Daniel" , "20")
d.speak()
d.works()
d.years()

