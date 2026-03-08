import random

while True:

    while True:
        
        try:
            emojis={'r': '🗿' ,'s':'✂️', 'p':'📃' }
            choices=('r','p','s')
            user_choice=input("Rock, paper or scissor (r/p/s)? ").lower()         #ask the user for choice
            if user_choice not in choices:
                print("Invalid choice!")     
            else:
                break        
        except ValueError:
            print("Invalid input! Try again.")   

    computer_choice = random.choice(choices)
    
    print(f"You chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Its a draw")
    elif((user_choice == 'r' and computer_choice== 's') or
        (user_choice == 'p' and computer_choice == 'r') or
        (user_choice == 's' and computer_choice == 'p') ):
        print("You win!")
    else:
        print("You lose!")

    play_again= input("Wanna play again? (y/n) ").lower()
    if play_again== 'y':
        continue
    elif play_again == 'n':
        break
    else:
        print("Invalid input!")