
class Box:
    id = 1000 #static property for the class Box
    def __init__(self):
        pass

    def doSomething(self):
        id = 2000

box1 = Box()
box2 = Box()



#overshadow the assignment property
box2.id = 5555
box2.id2 = 1000
box1.id2 = 'I am a new variable! Hello!'


print(box1.id) #print class property
print(box2.id) #print the new variable that we just created
print(box2.id2)
print(box1.id2)


