class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"x : {self.x}, y : {self.y}"
    
    def __eq__(self, other:"Point"):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self,other:"Point"):
        return self.x < other.x and self.y < other.y
    
# <= : le
# < : lt
# > : gt
# >= : ge
# != : ne
# == : eq

p1 = Point(10, 20)
p2 = Point(20, 18)
print(p1 == p2)
print(p1 < p2)