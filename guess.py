import random
lucky_num=random.randint(1,51)
def play_game():
    while True:
        user_num=int(input("Guess the number"))
        if user_num== lucky_num:
            print("You won!!")
            break
        elif user_num<lucky_num:
            print("Too low")
        else:
            print("Too high")

    print("Thank you for playing!!!")

play_game()