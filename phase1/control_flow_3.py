# if statement example

condition = True
if condition:
    print("Condition is True")
else:
    print("Condition is False")

# if-elif-else statement example
number = 10
if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")

# Nested if statement example
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not a citizen")
else:
    print("Too young")

# Ternary operator example
score = 85
result = "Pass" if score >= 60 else "Fail"
print(result)
scored = "pass" if score >=60 else "fail"
print(scored)   

num = 7

print("Even" if num % 2 == 0 else "Odd")

#what is the difference between % and // in python?The % operator is the modulus operator, which returns the remainder of a division operation. For example,
print(10 % 3)  # Output: 1
#The // operator is the floor division operator, which returns the quotient of a division operation, rounded down to the nearest whole number. For example,
print(10 // 3)  # Output: 3