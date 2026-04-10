# List 
#List ik order collection hothi hai jis mei muliple values store ho skthi hai List Features

#✔ Ordered ✔ Changeable (mutable) ✔ Duplicate allowed ✔ Different data types allowed

# Acessing element (indexing)
l1 = [1,3,2,4,5]
l2 = ['bzeem', 'Ali', 'Jamil']
l = [1,2,3,4,5]
l1.sort()
print(l1)
l2.sort()
print(l2)

print(l[0])
print(l[4])
print(l[1:5])
print(l[-1])

# Modifying element
l[0] = 10
print(l)
# Adding element
l.append(6) # add element at the end of the list
print(l)

# Removing element
l.remove(2) # remove the first occurrence of the specified value
print(l)
l.pop() # remove the last element of the list
l.pop(0) # remove the element at the specified index
print(l)
l.sort() # sort the list in ascending order
print(l)
l.sort(reverse=True) # sort the list in descending order
print(l)

# Set set unordered collection hotha hai dupicate values allow nai hothi
# Set Features
#✔ Unordered ✔ Unchangeable (immutable) ✔ No duplicate allowed ✔ Different data types allowed
# Faster than list because it uses hash table for storage
"""
A set is usually faster than a list for membership tests because a set is backed by a hash table, while a list is backed by a linear array.

For a list, checking whether an item exists often means scanning elements one by one, so it is 
O
(
n
)
O(n). For a set, Python hashes the item and jumps directly to the bucket where it should live, so lookup is usually 
O
(
1
)
O(1) on average.

That is why these operations are typically faster with a set:

membership checks
adding unique items
removing items
A list is still better when you need:

order preserved
duplicates allowed
indexed access by position
"""
# Acessing element (indexing)
s = {1,2,3,4,5}
print(s)
# Modifying element
#s[0] = 10 # TypeError: 'set' object does not support item assignment
# Adding element
s.add(6) # add element to the set in the end of the set
print(s)
# Removing element
s.remove(2) # remove the specified value from the set if the value not found it raises a KeyError
print(s)
s.discard(3) # remove the specified value from the set if the value not found it does nothing raise a KeyError
print(s)
s.pop() # remove and return an arbitrary set element. Raises KeyError if the set is empty.
print(s)
s.clear() # remove all elements from the set
print(s)
# Set Operations
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2)) # return a new set that is the union of s1 and s2
print(s1.intersection(s2)) # return a new set that is the intersection of s1 and s2
print(s1.difference(s2)) # return a new set that is the difference of s

#Tuple tuple bi list jaisa hotha hai lakin is ko change nai kr sktha Tuple Features

#✔ Ordered ✔ Immutable (change nahi ho sakta) ✔ Duplicate allowed ✔ Faster than list

# Access Element
point= (1,2)
print(point[0]) # return 0 index value 
# tuple modify nai hotha 
#point[0]=50 # its give error because tuple do not modify

#Single element tuple
t=(5)
print(t)
#Tuple packing and unpacking
data = (1,2,3)
a,b,c = data
print(a,b,c)

# ===================== TUPLE METHODS =====================

# In Python, tuple has only 2 built-in methods:
# 1) count()  → Returns the number of times a specified value appears.
# 2) index()  → Returns the index of the first occurrence of a specified value.

# ===================== IMPORTANT NOTE =====================

# Tuple is IMMUTABLE.
# That means:
# ✔ Values can be accessed
# ✘ Insert, append, remove, or modify operations are NOT allowed.

# ===================== ALLOWED OPERATIONS =====================

# 1) Indexing        → Access element using position number.
# 2) Slicing         → Access a range of elements.
# 3) len()           → Returns total number of elements.
# 4) Membership test → Using 'in' to check if value exists.
# 5) Iteration       → Using loop to traverse elements.

# ===================== EXAMPLE =====================
# tuple is Faster than list because it uses less memory and it is immutable

t = (5, 10, 15, 20, 5)

print(t.count(5))     # count()
print(t.index(10))    # index()
print(len(t))         # length
print(15 in t)        # membership
print(t[1:4])         # slicing
print(t[2])           # indexing

for x in t:           # iteration
    print(x)

# ===================== DICTIONARY (dict) =====================

# Dictionary is a built-in data structure used to store data in key-value pairs.
# It is mutable (values can be changed).
# Keys must be unique and immutable (string, number, tuple).
# Values can be of any data type.

# Example:
student = {
    "name": "Ali",
    "age": 21,
    "course": "CS",
    "marks": [80, 85, 90],
}
# ===================== IMPORTANT POINTS =====================

# ✔ Key-value based structure
# ✔ Mutable (can add, update, remove)
# ✔ Keys are unique
# ✔ Ordered (Python 3.7+)

# ===================== DICTIONARY METHODS =====================

# 1) keys()    → Returns all keys
# 2) values()  → Returns all values
# 3) items()   → Returns key-value pairs
# 4) get()     → Returns value of a key safely(not providing any error
# 5) update()  → Updates dictionary
# 6) pop()     → Removes specific key
# 7) clear()   → Removes all elements

# ===================== OPERATIONS EXAMPLE =====================

print(student.keys())        # keys()
print(student.values())      # values()
print(student.items())       # items()
print(student.get("name"))   # get()
student.update({"age": 22})  # update()
student.pop("course")     # pop()
print(student)
student.clear()              # clear()
print(student)