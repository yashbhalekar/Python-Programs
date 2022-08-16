usernames = ['jack','jessie','admin']

for username in usernames :
    if username != "admin" :
        print("Thank You" +" "+ username.title() + " for logging in")

    elif username == "admin":
        print("Admin! do you want to see status report")
        break

if not usernames :
    print("We need to find users")

