import random
playerInput = int(input("Pick rock (1) , paper (2), Scissors(3)."))
if playerInput == 1:
    playerInput = "rock"
elif playerInput == 2:
    playerInput = "paper"
elif playerInput == 3:
    playerInput = "scissors"
    

comp = random.randint(1,3)
if comp == 1:
    comp = "rock"
elif comp == 2:
    comp = "scissors"
if comp == 3:
    comp = "paper"



print(playerInput,'vs',comp )
if playerInput > comp:
    print("player wins!")
elif playerInput < comp:
    print("The computer wins!")
elif playerInput == comp:
    print("Tie !")