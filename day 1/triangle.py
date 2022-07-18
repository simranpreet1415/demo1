for x in range(1, 5):
    for y in range(1, x+1):
         print("*", end="")
    print()


for x in range(5):
    for y in range(5-x):
         print("*", end="")
    print()

# square
row = int(input("Enter number of rows: "))
print("Square pattern is: ")
for i in range(1,row+1):
    for j in range(1,row+1):
        print("*", end="")
    print()


# pyramid
row = int(input('Enter number of rows required: '))
for i in range(row):
    for j in range(row-i):
        print(' ', end='') # printing space required and staying in same line
    
    for j in range(2*i+1):
        print('*',end='') # printing * and staying in same line
    print() # printing new line

