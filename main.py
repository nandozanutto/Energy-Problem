#!/usr/bin/python2
from scipy.optimize import linprog
import sys
import inputsToSimplex as inSimplex
import DataConverting as configData


data = sys.stdin.read()#reading from stdin
inputLines = data.splitlines()#splitting the data into a string


h, l, R = inputLines[0].split()
h = int(h)
l = int(l)
R = int(R)

listHidro = []
listCentral = []
listArco = []

configData.convertData(h, l, listHidro, listCentral, listArco, inputLines)

c = inSimplex.vector(listHidro, listArco)
A = inSimplex.constraints(listCentral, h, listArco, listHidro)
b = inSimplex.results(listHidro, listCentral)
bounds = inSimplex.bounds(listHidro, listArco, R)

res = linprog(c, A_ub=A, b_ub=b, bounds=bounds)
resultList = res.x.tolist()
for x in range(0, h):
    resultList[x] = int(resultList[x]*listHidro[x].f)
for x in range(h, len(resultList)):
    resultList[x] = int(resultList[x])

print('\n'.join(map(str, resultList))) 
