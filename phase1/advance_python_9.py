# List Comprehension
l = [x*x for x in range(5)]
print(l)

# Dictionary Comprehension
nums=[1,2,3]
d = {x:x*x for x in nums}

print(d)

#Map Function
result = map(lambda x: x*x, range(5))
print(list(result))
# filter Function
result1 = filter(lambda x: x%2==0, range(10))
print(list(result1))
#lambda function
result3 = lambda x:x*x
print(result3(2))