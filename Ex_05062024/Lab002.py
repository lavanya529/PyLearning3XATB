print()
#self - Conecpt in OOps which points to inself. - ignore
#*args - Unlimited number of arguments * - strings, int , float, boolean..
#sep=' ' - How you want to separate the arguments
#end=' \n' - How you want to end the line.
#file=None - File IO.

print("Hello", "World", 123, True, 3.14)
# we can use unlimited number of arguments
print("Hello", "World", 123, True, 3.14, "Hello", "World", 123, True, 3.14)

print("Hello", "World", 123, True, 3.14, sep='#')
print("Hi , My Name is Lavanya", "Ganga", sep=' ')

#we can add anything as separator
#only one separator in one command
# cannot use separator first and then any other argument
print("Hello", "World", 123, True, 3.14, sep='@')