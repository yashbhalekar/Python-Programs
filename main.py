#INTRODUCTION TO LISTS

bicycles =['trek', 'redline', 'bmx' , 'hero' , 'hercules']
bicycles.append('firefox')
print(bicycles)
print(bicycles[1].upper())
message = "My dad gifted me"+ " " + bicycles[2].title() +" "+ "on my 5th Birthday"
print(message)
bicycles.insert(1,'goldie')
bicycles.insert(0,'robin')


print(bicycles)




cars=[]
cars.append('honda city')
cars.append('kia')
cars.append('santro')
print(cars)

print(cars)
cars.insert(1,'skoda')  #inserted a value in 1 place
print(cars)
del cars[1]
print(cars)
popped_car=cars.pop(0)
print(cars)
print("The last owned car is"+" "+popped_car.title()+".")
print("The car that is owned before santro was"+" "+popped_car.title())

#FOR
magicians = ["david","alice","carolina","harry"]
for magician in magicians:
    print(magician)
    print(magician.title()+" "+"that was a great trick")
    print("I cant wait to see next trick"+" "+magician.title())

print("Thank You everyone that was a great trick")

for value in range(0,5):
    print(value)

numbers =list(range(0,6))
print(numbers)

#SKIP THE NUMES USING RANGE
even_numbers = list(range(2 ,11,2))
print(even_numbers)

odd_numbers = list(range(0,12,3))
print(odd_numbers)

#PRINT SQUARES
squares =[]
for value in range(2,7):
    square = value**2
    squares.append(square)

print(squares)

#2nd METHOD
squares = [value**2 for value in range(2,7)]
print(squares)

players = ["charles","martin","micheal","eli"]
print("Here are first three names of players:")
for player in players[:3]:
    print(player.title())


#COPY A LIST USING : SLICE
myFoods = ['tomato','potato','onion','carrots']
friendsFoods = myFoods[ : ]

print("My foods are:")
print(myFoods)

print("My friends foods are:")
print(friendsFoods)