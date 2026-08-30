attempts = 0

while attempts < 3:

    username = input()
    password = input()

    if username == "Ramya" and password == "12345":
        print("Login successfully")
        break

    else:
        attempts = attempts + 1

        if attempts == 3:
            print("Maximum attempts reached")
        else:
            print("Try again")