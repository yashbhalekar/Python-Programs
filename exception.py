filename ='file1.txt'
try:
    with open(filename) as file_obj:
        contents =file_obj.read()
except FileNotFoundError:
    msg = "Sorry the file"+" "+filename+" "+"does not exist"
    print(msg)

else:
    words =contents.split()
    num_words=len(words)
    print("The"+" "+filename+" "+"has about"+str(num_words)+" "+"words." )