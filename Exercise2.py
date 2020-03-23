# -*- coding: utf-8 -*-
'''
    Escreva uma função

         def Solution(A, B)

    que, dadas duas listas A e B, que possuem N inteiros cada, retorna o número de valores em B que não aparecem em A.

    Por exemplo, dada uma lista A com 6 elementos conforme a seguir:
        
        A[0] = 2    A[1] = 1    A[2] = 1
        A[3] = 2    A[4] = 3    A[5] = 1

    E uma dada uma lista B, também com 6 elementos, como a seguir:

        B[0] = 2    B[1] = 0    B[2] = 1
        B[3] = 5    B[4] = 4    B[5] = 3


    a função deve retornar 3, pois existem 3 valores distintos que aparecem em B, mas não em A (0, 4 e 5).

    Escreva um algorítmo --eficiente-- para as seguintes suposições:

        - N é um inteiro no intervalo [0, 100.000];
        - Cada elemento das listas A e B é um inteiro no intervalo [-1.000.000, 1.000.000];
'''

def solution(A, B):
    return

inputs = [
    ([2, 1, 1, 2, 3, 1], [2, 0, 1, 5, 4, 3])
]

expecteds = [3]


for i in range(len(inputs)):
    result = solution(inputs[i][0], inputs[i][1])
    expected = expecteds[i]
    if result == expected:
        print ('OK')
    else:
        print ('Error while testing for %s. Expected %s, but got %s' % (inputs[i], expected, result))

