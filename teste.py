# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:10:45 2021

@author: Gustavo
"""

from __init__ import Desafio

lista_compras = [[], [], [] ]
lista_emails = ['nome@email.com', 'maria@email.com', 'joao@email.com']

dados = open('dataset_exemplo.csv', 'r')
for linha in dados:
    item, qtd, preco = linha.strip().split(',')
    qtd, preco = int(qtd), float(preco)
    lista_compras[0].append(item)
    lista_compras[1].append(qtd)
    lista_compras[2].append(preco)
dados.close()
    
API = Desafio(lista_compras, lista_emails)
resultado = API.retornaMapa()
for chave in resultado:
    print(chave,'pagará', resultado[chave], 'centavos')
