class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

def doOverlap(rect1, rect2):
    # If one rect is on left side of other 
    if(rect1.x1 >= rect2.x2 # rect 1 on right of rect 2
     or 
     rect2.x1 >= rect1.x2): # rect 2 on right of rect 1
        return False
    
    # If one rect is above other 
    if(rect1.y1 <= rect2.y2 # rect 2 on top of rect 1
     or 
     rect1.y2 >= rect2.y1): # rect 1 on top of rect 2
        return False 

    return True

rect1 = Rectangle(0, 10, 10, 0)
rect2 = Rectangle(5, 5, 15, 0)

print("Do Overlap" if doOverlap(rect1, rect2) else "Do not Overlap")

