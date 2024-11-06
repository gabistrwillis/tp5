import cmath


class Point:
    def __init__(self, *args):
        if len(args)==2:
            self.x=args[0]
            self.y=args[1]
        elif len(args)==1:
            p=args[0]
            self.x=p.x
            self.y=p.y

        if len(args)==0 or len(args)>2:
            raise ValueError('les arguments doivent de longueur 1 ou 2')

    def __getitem__(self, indice):
        if indice==0:
            return self.x
        elif indice==1:
            return self.y
        elif indice>1:
            raise IndexError("l'indice doit être compris entre 0 et 1")

    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'

    def __eq__(self, other):
        if self.x==other.x and self.y==self.y:
            return True

    def angle(self, otherpoint):
        vecteur.x=(otherpoint.x-self.x)
        vecteur.y=(otherpoint.y-self.y)
        return cmath.phase(complex(vecteur.x,vecteur.y))



p=Point(1,2)
p1=Point(p)
print(p1)
print(p)
p1==p