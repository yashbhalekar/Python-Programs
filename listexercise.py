#3.1

names = ['karan' ,'raj' , 'kris' , 'max']
print(names[0] )
print(names[1])
print(names[2])
print(names[3])

#3.2

message = "Hello..."+" "+names[0].title()+" "+"you are invited for the night party"
message_1= "Hello..."+" "+names[1].title()+" "+"you are  not invited for the night party"
message_2= "Hello..."+" "+names[2].title()+" "+"you are in waiting list for the night party"
message_3 = "Hello..."+" "+names[3].title()+" "+"you are invited for the night party"

print(message)
print(message_1)
print(message_2)
print(message_3)

#3.3

favorite_transport = ['honda_motorcycle' , 'bmw' , 'bus' ,'metro']
print("I regularly travel through"+" "+favorite_transport[-1].title()+" "+"and its a nice ride")
print("I would like to own a"+" "+favorite_transport[1].upper()+" "+"car")
print("My friend was gifted a"+" "+favorite_transport[0])


#3.4 #3.5 #3.6 #3.7

guest_list = ["grandpa","sister","bro","kevin","Olive"]
print("today"+" "+guest_list[0].title()+" "+"you are invited for the dinner")
print("today"+" "+guest_list[1].title()+" "+"you are invited for the dinner")
print("today"+" "+guest_list[2].title()+" "+"you are invited for the dinner")
print("today"+" "+guest_list[3].title()+" "+"you are invited for the dinner")
print("Sorry"+" "+guest_list[4].title()+" "+"couldn't make it")
guest_list.insert(0,'mom')
guest_list.insert(3,'dad')
guest_list.append("uncle")
print(guest_list)
print("Sorry to inform that"+" "+guest_list.pop()+" "+"due to shortage of table you are uninvited")
print("Sorry to inform that"+" "+guest_list.pop()+" "+"due to shortage of table you are uninvited")
print("Sorry to inform that"+" "+guest_list.pop()+" "+"due to shortage of table you are uninvited")
print("Sorry to inform that"+" "+guest_list.pop()+" "+"due to shortage of table you are uninvited")
print("Sorry to inform that"+" "+guest_list.pop()+" "+"due to shortage of table you are uninvited")
del guest_list



#3.8
bucket_list = ["Vegas","Spain","Paris","Amsterdam","Iceland"]
print(bucket_list)
print(sorted(bucket_list))
print(bucket_list)
bucket_list.reverse()   #REVERSE THE ORDER OF LIST
print(bucket_list)
bucket_list.reverse()
print(bucket_list)
bucket_list.sort()
print(bucket_list)
bucket_list.sort(reverse=True)
print(bucket_list)



#FINAL

cities = []
cities.append("Pune")
cities.append("Mumbai")
cities.append("Agra")
cities.append("Jodhpur")
cities.insert(1,"Jaipur")
cities.insert(3,"Banglore")
cities.insert(5,"Jhansi")
print(cities[0].upper()+" "+"is an historic city")
print(cities[2].title()+" "+"is the busiest city")
print(cities[4].title()+" "+"has Taj Mahal")
cities[3] ="Hyderabad"  #REPLACED A NEW CITY
print(cities)
cities.sort()
print(cities)
cities.sort(reverse=True)
print(sorted(cities))
print(cities)
del cities[5]   #DEL
print(cities)
cities.pop()
print(cities)   #POP
cities.remove("Jhansi")    #REMOVE
print(cities)

#4.1 BURGER
burgers = ["Mc_Aloo_Tikki","Chicken_Burger","Cheese_Burger"]
for burger in burgers:
    print(burger)
    print("I like"+" "+burger.title())

print("I really love Burgers")


#4.2 ANIMALS
animals = ["dog","cat","tiger"]
for animal in animals:
    print(animal)
    print(animals [0].title()+" "+"would be a great pet")
    print(animals[1].title()+" "+"are cute")
    print(animals[2].title()+" "+"are dangerous")

print




