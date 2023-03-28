from math import pi
from Figuras import Figuras

def test_square():
    figuras = Figuras()
    assert figuras.square(2) == 4

def test_rectangle():
    figuras = Figuras()
    assert figuras.rectangle(8,2)== 16   

def test_triangle():
    figuras = Figuras()
    assert figuras.triangle(8,8) == 64

def test_circle():
    figuras = Figuras()
    assert figuras.circle(2) == pi*2*2