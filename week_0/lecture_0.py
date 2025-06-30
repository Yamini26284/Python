# FUNCTIONS

''' 1. print is also a function that simply displays what ever input is given 
   to it inside a quotation marks which are enclosed in a paranthesis '''

#print(*object, sep=' ', end='\n', file=None, flush=False) # these are named parameters
## and these parameters are called positional parameters, given they print acccording to the positions 
print("hello", end="")# overridng the defualt print so that it doesnt go to the next line by specifing nothing in end ''
'''
   *object, sep=' ', end='\n', file=None, flush=False are the parameters in the print function's definition.
   The actual values you pass when you call print(), like "Hello", "World", "-", "...DONE!\n", etc., are the arguments.
'''
# *objects- print take any nomber of objects,we can pass from 0 strings to infinity

'''
1. error vs bug:
    An error is a human mistake in the code or design. An error is primarily a human mistake or oversight made by a 
    developer during any stage of the software development lifecycle
    A bug is the result of an error (or defect) in the software that causes it to behave unexpectedly or incorrectly
    Analogy:
    Think of building a house:

    Error: A human mistake like misreading the blueprints, using the wrong measurements, or accidentally putting a 
    nail through a water pipe during construction.
    Bug: The result of that mistake, such as a wall that's crooked, a door that doesn't close properly, 
    or a water leak that appears after the house is built.
'''
age = input("what is your age?:") #input is a function that has a return value and those return values are stored in variables
name = input("name: ")
'''
2. key points about the input() function in Python:

    1.Purpose: Used to get text input from the user via the console.
    2.Return Type: Always returns the input as a string (str), regardless of what the user types (e.g., numbers, words, symbols).
    3. Type Conversion: If you need numerical input (integers or floats), 
        you must explicitly convert the string using int() or float().
        Example: age = int(input("Enter your age: "))
    4.Prompt: Takes an optional single argument (a string) which serves as a prompt displayed to the user.
        Example: name = input("What's your name? ")
        input("123") is valid and will display "123" as the prompt.
    5.Error Handling: If you try to convert input to a type it doesn't match (e.g., int("hello")),
         it will raise a ValueError.     
    6.No Other Arguments: It accepts at most one argument (the prompt string). Passing more than one argument is a TypeError
'''

# function with multipe argumenats 
print("hey, I'm ",age) #hey, I'm  4  -->python automatically gives a space if it encounters multiple arguments in a function.
print("hey, I'm",age)  #hey, I'm 4

# this is a single argument which uses concatenation.
print("hey, I'm "+name+ " and I'm "+ age)  # hey, I'm prita and I'm 4
print("hey, I'm"+name+ "and I'm"+ age)     # hey, I'mpritaand I'm4


# STRINGS
''' str (Built-in Type/Class and Function):
strings can be used in two ways one as an object of string type and other str as a function :

   As a type/class, str defines what a string is and what operations (methods) can be performed on it. 
   When you create a string literal like "hello", you're creating an object of the str type.

   As a function, str() is used to convert other data types into their string representation. 
   For example, str(123) will return the string "123".

Why it's not a keyword, and what happens if you try to use it as a variable:
Because str is a built-in name and not a keyword, Python will allow you to use it as a variable name, 
but it's highly discouraged and considered a very bad practice. ''' 

# ARGUMENTS Vs PARAMETERS
'''
Parameters: These are the variables listed inside the parentheses in the function's definition (or declaration).
 They are placeholders for the values that the function expects to receive when it's called. 
 Parameters define the type and number of inputs a function can accept. They are part of the function's signature.

Arguments: These are the actual values that are passed to the function when it is called (invoked). 
Arguments are what fill the placeholders (parameters) during the function's execution.

'''
def greet(name, age): # name and age are PARAMETERS
   print(f"Hello, {name}! You are {age} years old.")

# Calling the function
greet("Alice", 30) # "Alice" and 30 are ARGUMENTS

# Another call with different arguments
greet("Bob", 25) # "Bob" and 25 are ARGUMENTS

# Formatted Strings
print(f"hello {name}")

# STRING methods
name = input("enter your name")
name=name.strip() 
# the strip() method in Python only removes whitespace from the beginning (leading) and end (trailing) of a string. 
# It does not remove whitespace in between the string.
print(name) 
'''
output: enter your name                 gabs            montane
                        ->gabs            montane
         enter your name    gabby motage       . 
                        ->gabby motage       .

'''

 