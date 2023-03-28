from math import pi

class Figuras:

    def square(self,l:int)->int:
        return l*l

    def rectangle(self,w:int,h:int)->int:
        return w*h
    
    def triangle(self,b:int,h:int)->int:
        return b*h
    
    def circle(self,r:int)->float:
        return pi*r*r
