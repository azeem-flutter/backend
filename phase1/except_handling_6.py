# Exception Handling 
# its safely execute the code if the error is occured then safely handled.
try:
    x = 10/0
except:
    print("Error Occured")

try:
    x = int("abc")
    y = 10 / 0
except ValueError:
    print("Conversion error")
except ZeroDivisionError:
    print("Division error")

# finally block 
# its always execute 
try:
    x = 5
    x= 10/0
    print(x)
except:
    print("Error")
finally:
    print("Done")

# else block 
# if the error is not appear then its runs this else block 
try:
     x = 5 
     x = 10/2
     x=10/0
     print(x)
except:
    print("Error")
else: 
    print("Done ")

# Real-world Example 
try:
    num = int(input("Enter number: "))
    print(10 / num)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")