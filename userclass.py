class User :
    def __init__(self,first_name,last_name,gender):
        self.f_name =first_name
        self.l_name =last_name
        self.gender =gender



    def describe_user(self):
        print("-- Summary of User -- ")
        print("First Name =>"+" "+self.f_name.title())
        print("Last Name =>"+" "+self.l_name.title())
        print("Gender =>"+" "+self.gender.title())


    def greet_user(self):
        print("Congratulations ! ,"+" "+self.f_name.title()+" "+"You are now member of GeekForGeeks")





user_info = User("daniel","wilson","male",1)
user_info.describe_user()
user_info.greet_user()


user_info2 = User("nancy","wills","female")
user_info2.describe_user()
user_info2.greet_user()

user_info3 = User("danny","knots","male")
user_info3.describe_user()
user_info3.greet_user()