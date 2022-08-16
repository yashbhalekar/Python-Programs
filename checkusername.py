current_users = ['John' ,'jonathan' ,'Will' ,'MAX' ,'Steve' ,'dustin']
new_users = ['Kinsy' ,'Will' ,'MAX' ,'catherine' ,'Clive' ,'clover']

for new_user in new_users :
    if new_user in current_users :
        print(new_user +" "+"will have to enter new username.")

    else :
        print("Username available")