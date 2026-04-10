# For Loop
# for loop is run fixed numbers of time . you can use it when you advance know how many time you want to repeat the code 
for i in range(5):
    print(i)
# For Loop with List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# For Loop with String
word = "Python"
for letter in word:
    print(letter)
# using enumerate to get index and value
for index,fruit in enumerate(fruits):
    print(index,fruit)

# Parallal iteration zip()
names = ["Ali", "Azeem"]
scores = [85, 90]
for name,score in zip(names,scores):
    print(name,score)

#List Comprehension (Single line)

l = [x**2 for x in range(5)]
print(l)
for i in l:
    print(i)

# While loop runs untill the condition is falls. you can use while loop when you not advance know how many time its repeat the code 
print("While Loop ")
i= 5
while i < 7:
    print(i)
    i +=1


# Break Statement 
# its used to break the loop
print("Break Statement")
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue Statement 
# its skip the current iteration and move to the next one

print("Continue Statement")
for i in range(10):
    if i == 5:
        continue
    print(i)

# Pass Statement
# its used as a placeholder for future code. it does nothing when executed
print("Pass Statement")
for i in range(5):
    pass
