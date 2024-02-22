from datetime import datetime

#With manages the closure of file
with open("my_file.txt") as file:
    contents = file.read()
    print (contents)


with open("my_file.txt", mode="w") as file:
    file.write("\nSome text written on {0}".format(str(datetime.now())))

with open("my_file_read_each_line.txt", mode="r") as file:
    lines = file.readlines()

for line in lines:
    print (line.strip())