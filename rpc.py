import random
import time

choices = ["rock", "paper", "scissors"]
rpc = "rock paper scissors"
words = rpc.split()

print("Rock Paper Scissors v1.0")
print("")

# initial
for word in words:
    print(word, end=" ", flush=True)
    time.sleep(0.5)
print()

pc_choice = random.choice(choices)
player_choice = input("Type your choice: ")
print("")

# who chose what
print(f"Pc chose => {pc_choice}")
print(f"You chose => {player_choice}")
print("")

# logic

    # same choice
if pc_choice == "rock" and player_choice == "rock":
    print("Coincidence?  Againnn!")
elif pc_choice == "paper" and player_choice == "paper":
    print("Coincidence?  Againnn!")
elif pc_choice == "scissors" and player_choice == "scissors":
    print("Coincidence?  Againnn!")

    # rock x paper
elif pc_choice == "rock" and player_choice == "paper":
    print("Paper covers rock, you WIN!!")
elif pc_choice == "paper" and player_choice == "rock":
    print("Paper covers rock, LOSER HAHAHA!!")

    # paper x scissors
elif pc_choice == "paper" and player_choice == "scissors":
    print("Scissors cuts paper, fair play!")
elif pc_choice == "scissors" and player_choice == "paper":
    print("Scissors cuts paper, need to wipe off your tears? :)")

    # rock x scissors
elif pc_choice == "rock" and player_choice == "scissors":
    print("Rock crashes scissors, try again?")
elif pc_choice == "scissors" and player_choice == "rock":
    print("Rock crushes scissors, bet you won't win next time!!")

   # invalid choices
else:
    print("That was a waste.")

print("")


# End
print("XOXO \n by Palccod")


