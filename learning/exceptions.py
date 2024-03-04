# File Error
try:
    file = open("a-non-existent-file.txt")
except FileNotFoundError:
    file = open("a-non-existent-file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print (f"Key {error_message} does not exist")
else:
    content = file.read()
    print (f"Content read {content}")
finally:
    file.close()
    print ("File was closed")
    raise KeyError("Made up error message") # or ValueError


# Raising own exception

# key Error
a_dict = {}
value = a_dict["a_key"]

# Index Error

# Type Error
# text = "abc"
# result = text + 5
