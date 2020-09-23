#params.py
#Mark Ashinhust CSE220 09/23/2020
#Description: Use of the '*' within parameter so we can use as many as we want. There is no limit as shown in print statements

#define method/function
def addThemAll(*numbers):
    total = 0
    for value in numbers:
        total += value
    return total

#print out our responses
print(addThemAll(1, 2, 3, 4, 5, 6, 7))
print(addThemAll(1, 2, 3))

end = input("Press ENTER to exit")
