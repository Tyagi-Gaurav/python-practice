#!/usr/bin/python3

dict = {"Bug" : "A value", 
        "Another Bug" : "Another value",
        123 : "An integer value"}

print (dict)
print (dict["Bug"])
print (dict[123])

#Adding
dict["NewKey"]= "Some new value"

print (dict)

for key in dict:
    print (key)
    print (dict[key])

#Nesting
nested = {
    "Barcelona" : ["La Rambla", "Familia Segrada", "Camp Nu"],
    "Rome" : {
        "visits" : 1,
        "places" : ["", ""]
    }
}

cities = ["Paris", "Delhi", "another city"]
print (cities)

cities.append("Berlin")
print (cities)