import cmath
import matplotlib.pyplot as plt


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
        vecteur = {'x':0,'y':0}
        vecteur.x=(otherpoint.x-self.x)
        vecteur.y=(otherpoint.y-self.y)
        return cmath.phase(complex(vecteur.x,vecteur.y))

    def distance_point(self,other):
        return cmath.sqrt((other.x-self.x)**2+(other.y-self.y)**2)


    def det(self, A, B):

        d=(A.x-self.x)*(B.y-self.y)-(B.x-self.x)*(A.y-self.y)
        return d
    '''
    Le signe du det va permettre de déterminer si le point self se situe en haut de la droite AB (si le det est >0) ou bien si le point se situe en bas de la droite (si le det est <0)
    '''

    def __lt__(self, other):
        return self<other







p=Point(1,0)
p2=Point(2,1)
p3=Point(1.5, 0)
print(p.distance_point(p2))
print(p3.det(p, p2))


class Points:
    def __init__(self,*v):
        self.l=[]
        for i in range (len(v)):
            self.l.append(Point(v[i]))

    def plot(self):
        plt.axis('equal')
        x=[i.x for i in self.l]
        y=[i.y for i in self.l]

        plt.scatter(x, y,color='green')
        plt.show()

    def extreme(self):
        x=[i.x for i in self.l]
        y = [i.y for i in self.l]
        min(x)

l= [Point(0,1),Point(1,0),Point(1,1)]
lp = Points( Point(0,1),Point(1,0),Point(1,1) )

print( lp.l[2])
lp.plot()
