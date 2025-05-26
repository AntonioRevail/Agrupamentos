# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 18:57:58 2019

""" Imports """
import random
import math

 
""" Support Functions """
def listToString(lst):
    strg = ''.join(lst)
    return strg

def split(word): 
    return [char for char in word] 

def replace(listOfBases):
    i = random.randint(-1,len(listOfBases)-1)
    possibilities = ['A', 'T', 'C', 'G', 'N', '-']
    if((listOfBases[i] == 'N') or (listOfBases[i] == '-')):
        possibilities.remove('N') 
        possibilities.remove('-') 
    else:
        possibilities.remove('N') 
        possibilities.remove('-') 
        possibilities.remove(listOfBases[i]) 
    listOfBases[i] = random.choice(possibilities)
    return listOfBases
    
def readBaseSequence(filePath):
    with open(filePath) as f:
        lines = f.read() 
        
    return split(lines)

def writeBaseSequence(filePath, newListOfBases):
    f = open(filePath, "a")
    f.write(listToString(newListOfBases) + '\n\n')
    f.close()

""" Main Code """
    

listOfBases = readBaseSequence('testebase.fas')
print("Numero de bases: " + str(len(listOfBases)))

""" Arredondamento para cima. Na prática, as bases costumam ter tamanhos superiores a 100. """
percentualToChange = 0.02 #0.01 = 1%
percentualToChange = random.uniform(0.0001,percentualToChange)
percentualToChange = 0.02
print("Percentual de bases a serem trocadas (%): " + str(percentualToChange*100.0))

countToChange = math.ceil((len(listOfBases)*percentualToChange))
print("Quantidade de bases a serem trocadas: " + str(countToChange))



""" print("Old sequence: " + str(listOfBases)) """

""" Chamar a função replace countToChange vezes """
for i in range(0, countToChange):
    listofBases = replace(listOfBases)
    
""" print("New sequence: " + str(listOfBases)) """
writeBaseSequence('resultadobase1.fas', listOfBases)


#print(listOfBases)




    
