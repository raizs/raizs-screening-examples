# -*- coding: utf-8 -*-
'''
    Escreva uma função

         def Solution(A)

    que, dada uma lista A, que possui N inteiros, retorna o número de valores distintos em A.

    Por exemplo, dada uma lista A com 6 elementos conforme a seguir:
        
        A[0] = 2    A[1] = 1    A[2] = 1
        A[3] = 2    A[4] = 3    A[5] = 1

    a função deve retornar 3, pois existem 3 valores distintos que aparecem em A (1, 2 e 3).

    Escreva um algorítmo --eficiente-- para as seguintes suposições:

        - N é um inteiro no intervalo [0, 100.000];
        - Cada elemento da lista A é um inteiro no intervalo [-1.000.000, 1.000.000];
'''

def solution(A):
    return

inputs = [
    [2, 1, 1, 2, 3, 1]
]

expecteds = [3]


for i in range(len(inputs)):
    result = solution(inputs[i])
    expected = expecteds[i]
    if result == expected:
        print ('OK')
    else:
        print ('Error while testing for %s. Expected %s, but got %s' % (inputs[i], expected, result))

