#!/usr/bin/python3

fruits = ["Apple", "Pear", "Peach"]
for fruit in fruits:
    print (fruit)

for n in range(1, 10):
    print (n)

print ("With Stepping")
sum = 0
target = 52
for n in range(0, target, 2):
  sum += n

print (sum)

for n in range(1, 6):
  print (n)
  if n == 4:
     n = n + 5
