# Consider the following code, which uses a while loop and found flag to search a list of powers of 2 for the value of 2 raised to the fifth power (32). It’s stored in a module file called power.py.

L = [1, 2, 4, 8, 16, 32, 64]
X = 5
found = False
i = 0
while not found and i < len(L):
    if 2 ** X == L[i]:
        found = True
    else:
        i = i+1
if found:
    print('at index', i)
else:
    print(X, 'not found')

# C:\book\tests> python power.py
# at index 5

# As is, the example doesn’t follow normal Python coding techniques. Follow the steps outlined here to improve it (for all the transformations, you may either type your code interactively or store it in a script file run from the system command line—using a file makes this exercise much easier):

# a)	First, rewrite this code with a while loop else clause to eliminate the found flag and final if statement. (2 marks)
L = [1, 2, 4, 8, 16, 32, 64]
X = 5
i = 0
while i < len(L):
    if 2 ** X == L[i]:
        break
    i = i + 1
else:
    i = -1

if i != -1:
    print('at index', i)
else:
    print(X, 'not found')

# b)	Next, rewrite the example to use a for loop with an else clause, to eliminate
# the explicit list-indexing logic. (Hint: to get the index of an item, use the list
# index method—L.index(X) returns the offset of the first X in list L.) (2 marks)
L = [1, 2, 4, 8, 16, 32, 64]
X = 5
value = 2 ** X

for item in L:
    if item == value:
        print('at index', L.index(item))
        break
else:
    print(X, 'not found')

# c)	Remove the loop completely by rewriting the example with a simple in
# operator membership expression. (2 marks)

L = [1, 2, 4, 8, 16, 32, 64]
X = 5
value = 2 ** X
if value in L:
    print('at index', L.index(value))
else:
    print(X, 'not found')

# d)	Use a for loop and the list append method to generate the powers-of-2 list (L) instead of hardcoding a list literal. (2 marks)
L = []
for i in range(7):  # assuming the original list had 7 elements
    L.append(2 ** i)

X = 5
value = 2 ** X
if value in L:
    print('at index', L.index(value))
else:
    print(X, 'not found')


