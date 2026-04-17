# Generator 
# Generator is a special type of function that return a lazy iterator. A generator produces a sequence of values one at a time, pausing its execution and maintaining its state between each yeild.
# A function called a generator if its contains atleast one yeild statement. When a generator function is called, it returns a generator object without executing the function. The generator can be iterated over using a loop or by calling the next() function.
#Key Concepts
# The yield Keyword: A function becomes a generator if it contains at least one yield statement. When yield is reached, the function's state is "frozen," and the value is returned to the caller.
# Lazy Evaluation: Generators do not compute or store all values at once. They produce values on-the-fly only when requested (e.g., in a for loop or via the next() function), making them highly memory-efficient for large datasets.
# Exhaustion: Once a generator has yielded all its values, it is "exhausted" and raises a StopIteration exception if called again. It cannot be restarted; you must create a new generator object to iterate again.
import sys
def creater():
    list1 = []
    i= 1 
    while i<=200:
        list1.append(i)
        i+=1
    return list1

print(creater())
print(sys.getsizeof(creater()))

# 
numbers = list(range(1,201))
print(numbers)
print(sys.getsizeof(numbers))

# Now the issue of the list is its contain a lot of memory inside the list. So to solve this issue we can use generator function instead of list.
def generator():
    i =1 
    while i<=200:
        yield i
        i+=1

gen = generator()
print(gen)
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(list(gen))
print(sys.getsizeof(gen))