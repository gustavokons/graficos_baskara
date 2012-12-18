'''
Created on Dec 17, 2012

@author: gustavokons
'''

from getopt import getopt
import sys
import function
import gerarHTML

args,args_rem = getopt(sys.argv[1:],"a:b:c:x:")

for ( param,valor ) in args:
    if param == '-a':
        a = valor
    elif param == '-b':
        b = valor
    elif param == '-c':
        c = valor
    elif param == '-x':
        x = valor
        
if function.ehNumeroInteiro(a) and function.ehNumeroInteiro(b) and function.ehNumeroInteiro(c):
    gerarHTML.gerarGrafico(int(a),int(b),int(c),x)
else:
    print 'ERRO de sintaxe\nSintaxe: python graficoBaskara.py -a valorInteiroA -b valorInteiroB -c valorInteiroC -x x1,x2,x3..xn'       
        