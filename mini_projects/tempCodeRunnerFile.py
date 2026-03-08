while True:
    try:
        choice=input("Rock, paper or scissor (r/p/s)? ").lower()       #ask the user for choice
        if choice not in ['r','p','s']:
            print("Invalid choice!")     
        else:
            break        
    except ValueError:
        print("Invalid input! Try again.")                  