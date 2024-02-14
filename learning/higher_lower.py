logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

import random
import higher_lower_data


def format_account(account):
    return f"{account['name']}, {account['description']}"

print (logo)
KeepGoing = True
score = 0
choice1 = random.choice(higher_lower_data.data)

while KeepGoing:
    choice2 = random.choice(higher_lower_data.data)

    print (f"Comparing A: {format_account(choice1)}")
    print (vs)
    print (f"Against B: {format_account(choice2)}")

    guess = input("\nWho has more followers? Type 'A' or 'B': ")

    if guess == 'A' and choice1["follower_count"] > choice2["follower_count"]:
        score = score + 1
        print(f"You're right!. Current Score: {score}")
    elif guess == 'B' and choice1["follower_count"] < choice2["follower_count"]:
        score = score + 1
        choice1 = choice2
        print(f"You're right!. Current Score: {score}")
    else:
        print("Sorry, that's wrong.")
        KeepGoing = False

print (f"Your Score {score}")