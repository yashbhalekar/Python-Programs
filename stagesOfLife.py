age = input("Enter the age of person =>")
age_of_person = int(age)


if age_of_person < 2 :
    print("The person is baby")

elif ( ( age_of_person>=2) and (age_of_person < 4))  :
    print("Person is  toddler")

elif  ((age_of_person >=4) and (age_of_person < 13 )) :
    print("Person is kid")

elif ((age_of_person >= 13) and (age_of_person < 20)) :
    print("Person is teenager")

elif((age_of_person >= 20) and (age_of_person < 65)) :
    print("Person is an adult")

else:
    print("Person is an elder")
