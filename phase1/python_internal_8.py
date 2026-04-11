# Memory Management
# Python uses a private heap to manage memory. All Python objects and data structures are stored in this private heap. The management of this private heap is ensured internally by the Python memory manager.
# Python has an inbuilt garbage collector, which recycles all the unused memory to make it
# pass by value vs pass by reference
# In Python, everything is an object, and variables are references to those objects. When you pass a variable to a function, you are passing a reference to the object, not the actual object itself. This means that if you modify the object within the function, it will affect the original object outside the function. However, if you reassign the variable within the function, it will not affect the original variable outside the function.
# A copy of the data is passed, so changes do not affect the original.
def change(x):
    x = x + 5
    print(x)

a = 10
change(a)

print(a)  # 10 (no change)
# A reference to the data is passed, so changes affect the original.
def change(lst):
    lst.append(4)
    print(lst)

a = [1, 2, 3]
change(a)

print(a)  # [1, 2, 3, 4] (changed)