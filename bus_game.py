player = []


while True:
    try:
        print("======BUS GAME MENU======")
        print("1.Add players")
        print("2.Start the game")
        print("3.Exit")
        print("==========================")
        
        option = int(input("Enter an option number: "))

        if option == 1:
            add_player()

        elif option == 2:
            start()

        elif option == 3:
            print("You have exited bus game!")
            break

        else:
            print("Invalid option entered. Try again!")

    except Exception as e:
        print("Error: ", e)