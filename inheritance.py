class Vehicle:
    def __init__(self,company,year,type):
        self.type =type
        self.comp =company
        self.year =year

    def work(self):
        print(self.comp +" "+"is an"+" "+self.type+" "+"type vehicle.")

    def fill_gas_tank(self):
        print(self.comp+" "+"needs a gas fill in")


class Car(Vehicle):
    def __init__(self ,company ,year ,type):
        super(Car, self).__init__(company , year , type)
        self.kilometers =450


    def kilom(self):
        print(self.comp+" "+"can go up to"+" "+str(self.kilometers)+"km")


tata =Car("TATA" ,"2020" ,"CnG")
tata.work()
tata.kilom()
tata.fill_gas_tank()
        #-------- ------------------CAR CLASS FINISHED-----------------------------

class MotorCycle(Vehicle):
    def __init__(self, company, year, type):
        super(MotorCycle, self).__init__(company, year, type)
        self.kilometer = 75

    def fill_gas_tank(self):
        print("This scooter doesn't need a gas" )

    def kilo(self):
        print(self.comp+" "+"runs for a distance of "+" "+str(self.kilometer)+"km.")


bike = MotorCycle("Tvs-iQube", "2019", "electric")
bike.work()
bike.kilo()
bike.fill_gas_tank()



