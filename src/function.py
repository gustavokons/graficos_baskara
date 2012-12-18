'''
Created on 05/12/2012

@author: gustavo
'''
from math import sqrt
import re

def getYFuncao(a,b,c,x):
    y = (a*(x*x)) - (b*x) + c
    return y


def zeroDaFuncao(a,b,c):
    raiz = (b*b) - (4*a*c)
    x1 = ( -b + sqrt(raiz) ) / ( 2*a )
    x2 = ( -b - sqrt(raiz) ) / ( 2*a )
    return [x1,x2]

def ehNumeroInteiro(numero):
    m = re.compile(r"\d*$")
    if re.match(m,numero):
        return True
    else:
        return False
