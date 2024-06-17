# Program to find the max in two numbers
print(max(10, 23))

print(max(10, 23, 45))
print(max(10, 23, 45, -1, -2, 100, 1, 87.34, 100.01))

# TypeError: '>' not supported between instances of 'str' and 'int'
#print(max(10, 23, 45, -1, -2, 100, 1, "Pramod"))

# here we will get error since complex number is not comparable
#print(max(10, 23, 45, -1, -2, 100, 1, 5 + 3j))
#print(max(10, 23, 45, -1, -2, 100, 1, complex(5, 3)))