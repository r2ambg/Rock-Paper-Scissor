import random
import sys

ValidGameInput = ["Rock", "Paper", "Scissor", "Quit"]
ValidGameOutput = ["Rock", "Paper", "Scissor"]
Win = 0
Lose = 0
Tie = 0
while True:
    print('%s Wins, %s Losses, %s Ties' % (Win, Lose, Tie))
    while True:
        UserInput = input("choose between Rock, Paper, Scissor :")
        GameOutput = str(random.choice(ValidGameOutput))
        print("Computer chose %s" % GameOutput)
        if UserInput == "Rock":
            print("you chose Rock")
            break
        elif UserInput == "Paper":
            print("you chose Paper")
            break
        elif UserInput == "Scissor":
            print("you chose Scissor")
            break
        elif UserInput == "Quit":
            print('%s Wins, %s Losses, %s Ties' % (Win, Lose, Tie))
            sys.exit()

    if UserInput == "Rock" and GameOutput == "Paper":
        print("You've lost")
        Lose = Lose+1

    if UserInput == "scissor" and GameOutput == "Paper":
        print("You've won")
        Win = Win+1

    if UserInput == "Rock" and GameOutput == "Scissor":
        print("You've lost")
        Lose = Lose+1

    if UserInput == "Paper" and GameOutput == "Scissor":
        print("You've Lost")
        Lose = Lose+1

    if UserInput == "Paper" and GameOutput == "Rock":
        print("You've Won")
        Win = Win+1

    if UserInput == "Scissor" and GameOutput == "Rock":
        print("You've Lost")
        Lose = Lose+1

    if UserInput == GameOutput :
        print("You've Tied")
        Tie = Tie+1
