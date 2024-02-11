#!/usr/bin/python3

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name1_lower = name1.lower()
name2_lower = name2.lower()

name_1_total = name1_lower.count("t") + name1_lower.count("r") + name1_lower.count("u") + name1_lower.count("e")

name_2_total = name1_lower.count("l") + name1_lower.count("o") + name1_lower.count("v") + name1_lower.count("e")

name_1_total += name2_lower.count("t") + name2_lower.count("r") + name2_lower.count("u") + name2_lower.count("e")

name_2_total += name2_lower.count("l") + name2_lower.count("o") + name2_lower.count("v") + name2_lower.count("e")

total = name_1_total * 10 + name_2_total

if total < 10 or total > 90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")
