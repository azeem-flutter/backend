# Decorator 
# Decorator is a function that takes another function as an argument and return a function.
# It is used to modify the behavior of a function without changing its code.

def decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

def hello():
    print(f'All Transaction steps')

decoratored_hello = decorator(hello)  # Decorating the function
decoratored_hello()  # Calling the decorated function

# Using @ symbol to decorate a function
@decorator
def hello():
    print(f'All Transaction steps')

hello()  # Calling the decorated function