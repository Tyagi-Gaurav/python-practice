numbers = [1, 2, 3]

print (numbers)
plus_one_list = [n + 1 for n in numbers]
print (plus_one_list)


squaring_list = [n * n for n in numbers]
print(squaring_list)

name = "Hello"
letters = [ch for ch in name]
print (letters)

double_range = [r * 2 for r in range(1,5)]
print (double_range)

# Conditional list comprehension
names = ["Gaurav", "Shyam", "Ram", "Laxman", "Raavan", "Jack"]
less_than_four_letter_names = [name for name in names if len(name) <= 4]

print (less_than_four_letter_names)

upper_case_names = [name.upper() for name in names if len(name) > 4]
print (upper_case_names)