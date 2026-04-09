num1 = int(input("Enter number1:"))
num2 = int(input("Enter number2:"))
num3 = eval(input("Enter number3:"))
print(num1 + num2)
print(num3)
"String Operations"
first = "Azeem"
last = "jamil"
# string is immutable you can not modify it using index
l=last.replace('a','z')
print(last)
print(l)
print(first + " "+ last)

f = "fayyaz"

print(f.replace('a','z'))
print(f)

# String Repetition 
print("Azeem"*3)

#String Indexing
word = "Python"
print(word[3])
print(word[-1])
print(word[-2])

# Slicing Part
word = "Artificial Intelligence"
print(word[0:13])
print(word[-1:-10:-1])
print(word[-1:-10:-2])

# Strip (Spaces Remove)
text = "   AI   "
print(text.strip())
# Strip (Spaces Remove)
text = "Hello AI"
print(text.replace("AI", "World"))
# Replace
text = "Hello AI"
print(text.replace("AI", "World"))
# Split
text = "AI is powerful"
a = text.split()
b = a[0]
print(b)
print(text.split())

# Find
# return the index of the first occurrence of the specified value. If the value is not found, it returns -1.
text = "Artificial Intelligencem Artificial Intelligence"
print(text.find("Intelligence"))
print(text.find("Artificial"))

# String formatting 
name = "Azeem"
age = 30
# this is the old method 
print("My name is ", name, "my age is", age)
# this is the Professional Method 
print(f"My name is {name} and I am {age} years old ")

# Checking in String 
text = "Artificial Intelligence"
print("Artificial" in text) # return True if the specified value is found in the string, otherwise it returns False.
print("Machine" in text) # return False

# Escaping Characters
print("Hello\nWorld")
print("Hello\tWorld")
print("Hello\" World")
print("HelloWorld")