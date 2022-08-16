rivers = {
    'egypt' : 'nile ',
    'india' : 'ganga ' ,
    'usa' : 'amazon',
}

for key, value in rivers .items() :
    print("\n Key :",key)
    print("\n Value :",value)

#PRINTS ONLY THE KEYS
for country in rivers.keys() :
    print(country.title())


 #PRINTS ONLY THE VALUES
for river in rivers.values() :
    print(river.title())
