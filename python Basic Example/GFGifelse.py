"""#python program to illustrate If statement
i = 10
if (i > 15):
    print('10 is less than 15')
print('I am Not in if')
"""

"""
i = 20
if (i < 15):
    print('i is smaller than 15')
    print('i"m in if Block')
else:
    print('i is greater than 15')
    print('i"m in else Block')
print('i"m not in if and not in else Block')
"""


"""
#Explicit function
def digitSum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum
#Initializing list
List = [367, 111, 562, 945, 6726, 873]

#Using the function on odd elements of the list
newList = [digitSum(i) for i in List if i & 1]

#Displaying new list
print(newList)
"""


"""
#Nested-if
i = 10
if (i == 10):
    #First if statement
    if (i < 15):
        print("i is smaller than 15")

    #Nested-if statement
    #Will only be executed if statement above
    #it is true
    if (i < 12):
        print('i is smaller than 12 too')
    else:
        print('i is greater than 15')
"""


"""
# If-else-elif statements
# Python program to illustrate if-elif-else ladder
i = 20
if (i == 10):
    print("i is 10")
elif (i == 15):
    print('i is 15')
elif(i == 20):
    print('i is 20')
else:
    print('i is not present')
"""



"""
#Short Hand If statement
#Python program to illustrate  short hand if
i = 10
if i < 15: print('i is less than 15')
"""


# Short Hand if-else statement
i = 10
print(True) if i < 15 else print(False)