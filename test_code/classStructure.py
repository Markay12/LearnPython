
class Box:
    id = 1000 #static property for the class Box
    def __init__(self):
        pass

box1 = Box()
box2 = Box()

box2.id = 5555

print(box1.id)
print(box2.id)

