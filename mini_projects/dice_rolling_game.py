import random

while True:
    choice= input("Role the dice? (y/n): ").lower()
    if choice == "y":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"{dice1},{dice2}")
    elif choice == "n":
        print("thank you for playing!")
        break
    else:
        print("invalid choice")


# Modify the program so the user can specify how many dice they want to roll
while True:

    choice= input("Role the dice? (y/n): ").lower()

    if choice == "y":
        num_of_dice=int(input("how many dices you wanna roll?: "))
        results = []
        for i in range(num_of_dice):
            results.append(random.randint(1, 6))
        print(results)
            
    elif choice == "n":
        print("thank you for playing!")
        break
    else:
        print("invalid choice")


# Add a feature that keeps track of how many times the user has rolled the dice during the session. 
counter=0
total_dice=0

while True:
    choice = input("Role the dice? (y/n): ").lower()

    if choice == "y":
        counter+=1

        num_of_dice=int(input("how many dices you wanna roll?: "))

        total_dice=total_dice+num_of_dice

        results = []
        for i in range(num_of_dice):
            results.append(random.randint(1, 6))
        print(results)
        print("Dice rolled this turn:", len(results))
            
    elif choice == "n":
        print("thank you for playing!")
        break
    else:
        print("invalid choice")

print(f"You rolled dice {counter} times during the session")
print(f"NUmbers of times dice rolled throughout session: {total_dice}")