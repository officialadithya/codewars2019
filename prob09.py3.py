inputLst = []
inputLst = input().split()
choice1 = inputLst[0].lower()
choice2 = inputLst[1].lower()
if choice1 == "scissors":
    if choice2 == "rock":
        print("SCISSORS LOSES, Rock crushes Scissors")
    elif choice2 == "paper":
        print("SCISSORS WINS, Scissors cut Paper")
    elif choice2 == "lizard":
        print("SCISSORS WINS, Scissors decapitates Lizard")
    elif choice2 == "spock":
        print("SCISSORS LOSES, Spock smashes Scissors")
    else:
        print("TIE, SCISSORS does not affect SCISSORS")
elif choice1 == "paper":
    if choice2 == "scissors":
        print("PAPER LOSES, Scissors cut Paper")
    elif choice2 == "rock":
        print("PAPER WINS, Paper covers Rock")
    elif choice2 == "lizard":
        print("PAPER LOSES, Lizard eats Paper")
    elif choice2 == "spock":
        print("PAPER WINS, Paper disproves Spock")
    else:
        print("TIE, PAPER does not affect PAPER")
elif choice1 == "rock":
    if choice2 == "scissors":
        print("ROCK WINS, Rock smashes Scissors")
    elif choice2 == "paper":
        print("ROCK LOSES, Paper covers Rock")
    elif choice2 == "lizard":
        print("ROCK WINS, Rock crushes Lizard")
    elif choice2 == "spock":
        print("ROCK LOSES, Spock vaporizes Rock")
    else:
        print("TIE, ROCK does not affect ROCK")
elif choice1 == "lizard":
    if choice2 == "scissors":
        print("LIZARD LOSES, Scissors decapitates Lizard")
    elif choice2 == "paper":
        print("LIZARD WINS, Lizard eats Paper")
    elif choice2 == "rock":
        print("LIZARD LOSES, Rock crushes Lizard")
    elif choice2 == "spock":
        print("LIZARD WINS, Lizard poisons Spock")
    else:
        print("TIE, LIZARD does not affect LIZARD")
elif choice1 == "spock":
    if choice2 == "scissors":
        print("SPOCK WINS, Spock smashes Scissors")
    elif choice2 == "paper":
        print("SPOCK LOSES, Paper disproves Spock")
    elif choice2 == "lizard":
        print("SPOCK LOSES, Lizard poisons Spock")
    elif choice2 == "rock":
        print("SPOCK WINS, Spock vaporizes Rock")
    else:
        print("TIE, SPOCK does not affect SPOCK")

