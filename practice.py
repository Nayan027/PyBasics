player = input("\nEnter player name: ")
print("Hello", player, "welcome to the game of uncertainty!!")

move = input("\nshould we move forward? Are you ready to play? (yes/no): ").lower()

if move == "yes":
    print("\nokay, let's begin with the game.")

    weapon = input("\nchoose a weapon of your choice (stick/ axe/ pen/ sword): ").lower()
    if weapon == "sword":
        print("you have chosen sword as a weapon against your opponent")
        direction = input("\nchoose your surprise opponent moving forward pick from (A/B/C): ").lower()

        if direction == "a":
            print("\nyour opponent has a stick. Thus You won!!!!!")
        
        elif direction == "b":

            decide = input("\nyour opponent has an axe. Would you fight or submit? :").lower()
            if decide == "fight":
                print("You've fought well.... you're a winner.")
            elif decide == "submit":
                print("You gave up before fighting... you're a loser.")
            else:
                print("you messed up making a choice... try again.")

        elif direction == "c":
            print("\nyour opponent has a pen. Thus You won!!!!!")

        else:
            print("\nInvalid direction....try again.")


    elif weapon == "pen":
        print("you have chosen pen as a weapon against your opponent")
        direction = input("\nchoose your surprise opponent moving forward pick from (A/B/C): ").lower()

        if direction == "a":
            decide = input("\nyour opponent has an stick. Would you fight or submit? :").lower()

            if decide == "fight":
                print("You've fought well.... you're a winner.")
            elif decide == "submit":
                print("You gave up before fighting... you're a loser.")
            else:
                print("you messed up making a choice... try again.")

        elif direction == "b":
                print("Your opponent has an axe. Sorry you ded...")

        elif direction == "c":
            print("\nyour opponent has a sword. Sorry you ded...")

        else:
            print("\nInvalid direction....try again.")




    elif weapon == "axe":
        print("you have chosen axe as a weapon against your opponent")
        direction = input("\nchoose your surprise opponent moving forward pick from (A/B/C): ").lower()

        if direction == "a":
            print("\nyour opponent has a stick. Thus You won!!!!!")
        
        elif direction == "b":

            decide = input("\nyour opponent has a sword. Would you fight or submit? :").lower()
            if decide == "fight":
                print("You've fought well.... you're a winner.")
            elif decide == "submit":
                print("You gave up before fighting... you're a loser.")
            else:
                print("you messed up making a choice... try again.")

        elif direction == "c":
            print("\nyour opponent has a pen. Thus You won!!!!!")

        else:
            print("\nInvalid direction....try again.")





    elif weapon == "stick":
        print("you have chosen stick as a weapon against your opponent")
        direction = input("\nchoose your surprise opponent moving forward pick from (A/B/C): ").lower()

        if direction == "c":
            decide = input("\nyour opponent has an pen. Would you fight or submit? :").lower()

            if decide == "fight":
                print("You've fought well.... you're a winner.")
            elif decide == "submit":
                print("You gave up before fighting... you're a loser.")
            else:
                print("you messed up making a choice... try again.")

        elif direction == "a":
                print("Your opponent has an axe. Sorry you ded...")

        elif direction == "b":
            print("\nyour opponent has a sword. Sorry you ded...")

        else:
            print("\nInvalid direction....try again.")

    else:
        print("Please pick a weapon from the given options only!!! Try Again.")

elif move == "no":
    print("\nokay, we'd love to have u play some other time soon.")
else:
    print("\nInvalid input, please try again!")