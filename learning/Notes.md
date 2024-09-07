* An important characteristic of the Python language is the consistency of its object model. Every number, string, data structure, 
function, class, module, and so on exists in the Python interpreter in its own “box,” which is referred to as a Python object. 

* Each object has an associated type (e.g., integer, string, or function) and internal data. In practice this makes the language very 
flexible, as even functions can be treated like any other object.

* Variables are names for objects within a particular namespace; the type information is stored in the object itself.

* In Python, a module is simply a file with the .py extension containing Python code.

* A common use of is and is not is to check if a variable is None, since there is only one instance of None

* Python has a small set of built-in types for handling numerical data, strings, Boolean (True or False) values, and dates and time. These
"single value" types are sometimes called scalar types

* f-strings for formatted strings
* r-strings for raw strings

* Note that list concatenation by addition is a comparatively expensive operation since a new list must be created and the objects copied 
over. Using extend to append elements to an existing list, especially if you are building up a large list, is usually preferable

* You can select sections of most sequence types by using slice notation, which in its basic form consists of start:stop passed to the 
indexing operator []:

* A generator is a convenient way, similar to writing a normal function, to construct a new iterable object. Whereas normal functions 
execute and return a single result at a time, generators can return a sequence of multiple values by pausing and resuming execution each 
time the generator is used. To create a generator, use the yield keyword instead of return in a function.
