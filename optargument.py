def name(first_name ,last_name ,middle_name=' ') :
    if middle_name:
        full_name = first_name +" "+middle_name+" "+last_name
    else:
        full_name =first_name+" "+last_name
        return full_name.title()

musician =name('jim','lee')
print(musician)

musician =name('jim','henry','hooker')
print(musician)