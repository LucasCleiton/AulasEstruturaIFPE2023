# -*- coding: utf-8 -*-
"""ED_AT02|09112023

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZBYFwUEjQs7nAzFJhizFFXd5x2qMmUaC
"""

"""
Exercício 3:
 Maior e Menor Elemento  Escreva um programa que
 encontre o maior e o menor elemento em uma lista de números inteiros.
"""

lista=[14,15,16,22,100,33,999,1212,4,5,0,32]

menor=lista[0]
maior=lista[0]

for i in range(len(lista)):
  if lista[i] > maior :
    maior = lista[i]
  if lista[i] < menor:
    menor = lista[i]


print(f"o maior numero da lista é {maior} e  menor :{menor}")