filename = 'file.txt'
with open(filename) as file_obj:
    for line in file_obj:
        print(line.rstrip())


#WRITING TO A FILE
filename='file.txt'
with open(filename,'w') as obj:
    obj.write("I love programming.\n")
    obj.write("I love Python.\n")
    obj.write("I love Flask.")


#APPENDING THE FILE
filename='file.txt'
with open(filename,'a') as obj:   #'a' appends the info rather than overwriting
    obj.write("I love programming.\n")
    obj.write("I love Python.\n")
    obj.write("I love Flask.")



