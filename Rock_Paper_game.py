import random
import time

a = ["stone", "paper", "scissor"]
print("lets start the game \nThere will be 3 rounds \n")
time.sleep(1)
print("\t  3")
time.sleep(1)
print("\t  2")
time.sleep(1)
print("\t  1")
time.sleep(0.5)
print("\n\tlets go !!!!\n")

# print(random.choice(a))

PlayerPoints = 0
CompPoints = 0
i = 1
while i <= 3:
    player = input("enter your move :  ").strip()
    r = random.choice(a)
    print("computer :  {}".format(r))

    if player.lower() == r:
        print("tie")

    ######################################################################

    elif player.lower() == "stone" and r == "scissor":
        PlayerPoints += 1
        print("You win !!!")

    elif player.lower() == "stone" and r == "paper":
        CompPoints += 1
        print("You lost")

    #######################################################################

    elif player.lower() == "paper" and r == "stone":
        PlayerPoints += 1
        print("You win !!!")

    elif player.lower() == "paper" and r == "scissor":
        CompPoints += 1
        print("You lost !!!")

    #######################################################################

    elif player.lower() == "scissor" and r == "stone":
        # CompPoints += 1
        print("You lost !!!")
        CompPoints += 1

    elif player.lower() == "scissor" and r == "paper":
        # PlayerPoints += 1
        print("You win !!!")
        PlayerPoints += 1
    i += 1

time.sleep(1)
print("\nYour Points : {} \nComputer Points : {}".format(PlayerPoints, CompPoints))
if PlayerPoints == CompPoints:
    print("Its a tie")
elif PlayerPoints > CompPoints:
    print("Congrats, You win this game !!!!!!!")
elif PlayerPoints < CompPoints:
    print("You lost this game . Better Luck next time .")
