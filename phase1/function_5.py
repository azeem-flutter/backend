# Function 
# A function is a reusable block of code that performs a specific task. It can take input parameters and return output. Functions help to break down complex problems into smaller, manageable pieces, promote code reusability, and improve readability.

def greet(name):
    print(f"Hello {name}")

greet("Azeem")

# Arguments and Parameters
def add(a, b):
    print(a+b)

add(5, 10)

# Arguments Types
# Positional Arguments 
# Values are passed based on Position 
def sum(a,b):
    print(a+b)

sum(5,10)
# Keyword Arguments
# Values are passed based on Keyword . Not based on position
def sum(a,b):
    print(a+b)
sum(b=5,a=10)

# Default Arguments
# If no value is provided for a parameter, the default value will be used
def greet(name="Guest"):
    print(f"Hello {name}")
greet()  # Output: Hello Guest
greet("Azeem")  # Output: Hello Azeem

# Variable positional Arguments (*args)
# Allows a function to accept an arbitrary number of positional arguments. Inside the function, args is treated as a tuple containing all the passed arguments.
def sum(*args):
    total = 0
    for num in args:
        total += num
    print(total)
sum(1, 2, 3)  # Output: 6
sum(4, 5)     # Output: 9

# Variable keyword Arguments (**kwargs)
# Allows a function to accept an arbitrary number of keyword arguments. Inside the function, kwargs is treated as a dictionary containing all the passed keyword arguments.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Azeem", age=30, city="Karachi")

# Return Funtion 
# Function return can return a value using the return statement. Once a return statement is executed, the function terminates and returns the specified value to the caller.
# if return statement is not used in a function, it will return None by default
def add(a, b):
    return a + b
result = add(5, 10)
print(result)  # Output: 15

#What is a First-Class Function?

#👉 Definition:

#A function is called first-class if it can:

#Be assigned to a variable
#Be passed as an argument
#Be returned from another function

# Example of First-Class Function
def greet(name):
    return f"Hello {name}"  
greeting = greet  # Assigning function to a variable
print(greeting("Azeem"))  # Output: Hello Azeem

def call_function(func, name):
    return func(name)  # Passing function as an argument
print(call_function(greet, "Azeem"))  # Output: Hello Azeem

def outer_function():
    def inner_function(name):
        return f"Hello {name}"  # Returning a function from another function
    return inner_function
greet_func = outer_function()
print(greet_func("Azeem"))  # Output: Hello Azeem

# Variable Scope 
# Local Variable 
# Local variables only accessible inside a function 

def test():
    x=10
    print(x)

test()
#print(x) its give error because the x is a local variable 

# Global Variable 
# Variables that can access inside and outside the function. and its also define outside the function 
x= 20
def test1():
    x= 30 # now its only re-assign  it inside a function so know x is 30 but outside x is 20
    print(x)

test1()
print(x)
# Modify the Global Variable inside a function 
y= 40
def test2():
    global y
    y = 30
    print(y)
test2()
print(y)

# Lamada Function 
#👉 One-line anonymous function
#👉 Naam nahi hota

square = lambda x: x*x
print(square(2)) # return the value 4

# Map function 
# its apply function to all elements 
nums = [1,2,3,4]
result = list(map(lambda x: x*x, nums))
print(result)

# Filter function 
# if the codition is true then its keep the element 

result1 = list(filter(lambda x: x%2==0, nums))
print(result1)