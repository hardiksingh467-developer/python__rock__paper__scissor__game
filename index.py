# dependency imports
import random 
# file imports

# Maintain a Dictionary for choices
availableChoices = {1: {"element": "Rock", "defeatedBy": 2}, 2: {"element": "Paper", "defeatedBy": 3}, 3: {"element": "Scissors", "defeatedBy": 1}}

# First ask fro user inputs
print("Please choose between by entering the corresponding number :-")
for key, value in availableChoices.items():
    print(f"{key} : {value['element']}")
userChoice = input();

try:
    userChoice = int(userChoice)
    if(type(userChoice) is not int or userChoice not in availableChoices.keys()): raise ValueError
except ValueError:
    print("Invalid Choice, Please try again")
    exit(0)

# Let the user know about their choice of selection
print("You've selected : ", availableChoices[userChoice]["element"])

# Let the computer know about their choice of selection
computerChoice = random.choice(range(1, 4))
print("Computer Chose", availableChoices[computerChoice]["element"])

if computerChoice == userChoice:
    print("The game ended in a Tie")
    exit(0)

if availableChoices[computerChoice]["defeatedBy"] == userChoice:
    print("You won")
    exit(0)

print("Computer won")
exit(0)