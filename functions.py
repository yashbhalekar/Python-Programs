def greet_user(username) :
    print("hello"+username.title()+"!")


greet_user("Harry")


#POSITIONAL ARGUMENTS
def pet_info(pet_type,pet_name) :
    print("I have a "+" "+pet_type.title()+" "+"and his name is "+" "+pet_name.title()+".")


pet_info("hamster","roy")   #FUNCTION CALL
#MULTIPLE FUNCTION CALLS
pet_info("dog","willie")
pet_info("cat","snowbell")
pet_info("horse","max")

#KEYWORD ARGUMENTS
pet_info(pet_type="rabbit" ,pet_name="peter")
pet_info(pet_name="rocky" ,pet_type="white mouse") #THE ORDER DOES NOT MATTER IN KEYWORD ARGUMENTS


#RETURNING VALUE USING FUNCTION
def name(f_name,l_name) :
    full_name= f_name +" "+l_name
    return full_name.title()

musician =name("joy","collins")

print(musician)

#OPTIONAL ARGUMENT
def person_name(first_name,last_name,middle_name=' ') :
    if middle_name :
        full_name = first_name +" "+middle_name+" "+last_name
    else:
        full_name =first_name+" "+last_name
        return full_name.title()

band =person_name("jim","hooker")
print(band)

band =person_name("jim","henry","hooker")
print(band)

#PASSING A LIST

def greet_users(names) :
    for name in names :
        msg= "Hello"+" "+name.title()+"."
        print(msg)

usernames = ['jimi','josh','drake']
greet_users(usernames)