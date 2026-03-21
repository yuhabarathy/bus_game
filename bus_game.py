player = []
s_num = 1

def add_player():
    num = int(input("Enter the total no.of players: "))
    for i in range(num):
        name = input(f"Enter name of player {i+1}: ")
        player.append(name)
    
    print("Players added successfully!")
    for data in player:
        print(data, end=" ")

def start():
   global s_num
   if len(player) < 2:
        print("Add atleast 2 players!")
        return

   while (len(player) > 1):
    i=0

   while i < len(player):
        print("="*10 , end=" ")
        print(f"\n{player[i]}'s turn")
        print("="*10)

        ans = input("Enter number: ").lower()

        if ans == "bus" and s_num%5 == 0:
            print("correct!")
            s_num += 1

        elif int(ans) == s_num and s_num%5!= 0:
            print("correct!")
            s_num += 1
            i+=1

        else:
            print(f"{player[i]} wrong answer!")
            player.pop(i)
            s_num += 1

            if len(player) == 1:
                print(f"\nPlayer {player[0]} Won, congratulation!")
                return
        

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