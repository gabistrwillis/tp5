

class Point:
    def __init__(self, *args):
        if len(args)==2:
            self.x=args[0]
            self.y=args[1]
        if len(args)==0 or len(args)==1 or len(args)>2:
            return None


p=Point(1,2)
print(Point(p))