# python-practice

* `bob = ['Bob Smith', 42, 30000, 'software']` 
* `sue = ['Sue Jones', 45, 40000, 'hardware']`
* `people = [bob, sue]`
* `for person in people:
        print (person)
  `
* `pays = [person[2] for person in people]`
* `pays = map(lambda x: x[2], people)
* Sum of Salarys `sum(person[2] for person in people)`
* `people[-1]` #Negative index is used in python to index starting from the last element of the list

* Creating virtual environment: `virtualenv -p $( which python3 ) .lpvenv`
    -> or `python3 -m venv myenv`

* Activate Virtual Environment: `source .lpenv/bin/activate`

* Python Scopes (Order in which object are found - LEGB)
    * Local Scope: Innermost scope that contain local names
    * Enclosing Scope: Scope of any enclosing function. Contains non-local names and also 
    non-global names.
    * Global Scope: Contains global names.
    * Built-in Scope: Contains built-in names.
    
* Magic Methods
    * Every method that has leading and trailing double underscore, in Python, is called magic 
    method. Magic methods are used by Python for a multitude of different purposes, hence 
    it's never a good idea to name a custom method using two leading and trailing 
    underscores. This naming convention is best left to Python.
    
* Indexing and Slicing Strings
    * `s[0]`
    * `s[:]` - Get a copy of the String
    * `s[2:14:3]` - Slicing from 2nd character, upto 14th and step 3
    * `s[::-1]` - Reverse a string

* PyPi (Python package index)
  * 

# Sequence to make Snake Game and/or anything else
* Install PyCharm
* BandGenerator
* (/) Number of weeks left assuming you live till 90
* (/) Odd or even number
* (/) Leap Year checks
    * To be a leap year, the year number must be divisible by four – except for end-of-century years, which must be divisible by 400. This means that the year 2000 was a leap year, although 1900 was not.
* (/) Print Array
    * Given an array of numbers, print the numbers to the console.
* (/) Sum of elements in Array
    * Given an array of numbers, find the sum of all the numbers
* (/) Average of elements in Array
    * Given an array of numbers, find the average of all the numbers
* For loops and range function
    * Using for loop to print elements of an array
    * Using for loop to sum elements of an array
    * Using for loop to print elements at 
* While loops
* Add digits of a number - Using string --> DataType conversion
    * Given a number, add the digits of the number
* writing simple function
* Factorial
* Looping in dictionary example to store bids and find highest bidder.
* Given a month, find days in a month
* Calculator - Simple
* Blackjack
* Scope - Local v Global
    * There is no Block Scope in Pythin
    * How to modify Global variable
* Number guessing game
* Higher & Lower
* Coffe Machine
* Coffee Machine OOP
* Quiz Game (OpenTDB)
* Inheritance

# References
* Python Tutor
* Reeborgs code
