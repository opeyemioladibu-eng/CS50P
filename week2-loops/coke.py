# ask for user input i.e insert a coin in 25,10,5 cents
Owed = 50
while True:
        user_input = (input("Insert Coin [25/10/5 Cents]:"))
        if user_input == "25":
            Owed -= 25
            print(f"Amount due:{Owed}")
        elif user_input == "10":
            Owed -= 10
            print(f"Amount due: {Owed}")
        elif user_input == "5":
            Owed -= 5
            print(f"Amount due:{Owed}")
        else:
            print("Only 25/10/5 Cents are accepted")
        if Owed <= 0:
            break
print(f"Change Owed:  {abs(Owed)}")
        