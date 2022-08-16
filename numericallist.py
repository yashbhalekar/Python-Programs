#4.3
numbers = []
for value in range(1,21):
    count= value
    numbers.append(count)

print(numbers)

list_of_nums = []
for value in range(1,1000000):
    add=value
    list_of_nums.append(add)

print(list_of_nums)
print(max(list_of_nums))
print(min(list_of_nums))
print(sum(list_of_nums))


#4.6
nos = list(range(1,21,5))
print(nos)

#4.10
items_list = ['amul milk','bread','chicken','eggs','brocolli','carrots']
print("First three items are:")
for item in items_list[0:3]:
    print(item)

print("Middle three items from list are:")
for item in items_list[1:4]:
    print(item)


print("Last three items from list are:")
for item in items_list[3:6]:
    print(item)


#4.11
myBikes = ['honda','suzuki','tvs']
friendBikes = myBikes[:]
myBikes.append("bmw".upper())
friendBikes.append("ola")
print("My bikes are:")
print(myBikes)
print("Friends bikes are:")
print(friendBikes)

