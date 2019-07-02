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