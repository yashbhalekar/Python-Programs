class Restaurant:

    def __init__(self,restaurant_name ,cuisine_name):
        self.rn =restaurant_name
        self.cn =cuisine_name



    def describe_restaurant(self):
        print("restaurant name :"+self.rn)
        print("restaurant cuisine :"+self.cn)


    def open_restaurant(self):
        print("The restaurant "+" "+self.rn+" "+"is open")

 #----------------------------------INCOMPLETE PG-178
class IceCreamStand(Restaurant):
    def __init__(self , restaurant_name ,cuisine_name):
        super(IceCreamStand, self).__init__(restaurant_name , cuisine_name)
        self.flavors =['chocolate' ,'strawberry' ,'mango']

    def display_flavours(self):
        print(self.rn +" "+"has"+" "+self.flavors+"ice-cream flavors")

#--------------------------------END

info = Restaurant ("Blue Nile" ,"Italian")
info.describe_restaurant()
info.open_restaurant()




info2 = Restaurant ("George" ,"Chinese")
info2.describe_restaurant()
info2.open_restaurant()

info3 = Restaurant ("Garden Court" ,"Spanish")
info3.describe_restaurant()
info3.open_restaurant()