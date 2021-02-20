# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15

@author: Gustavo
"""

import pagamentos

#caminhoCompras = input("Insira o caminho do dataset com as compras: ")
#caminhoEmails = input("Insira o caminho do dataset com os emails: ")

caminhoCompras = 'dados/datasetCompras_exemplo.csv'
caminhoEmails = 'dados/datasetEmails_exemplo.csv'

lista_compras = [[], [], [] ]
print("-- Lendo dataset com as compras --")
dadosCompras = open(caminhoCompras, 'r')
for linha in dadosCompras:
    linha = linha.strip()
    item, qtd, preco = linha.split(',')
    qtd, preco = int(qtd), float(preco)
    lista_compras[0].append(item)
    lista_compras[1].append(qtd)
    lista_compras[2].append(preco)
    print(linha)
dadosCompras.close()

lista_emails = []
print("\n-- Lendo dataset com os emails --")
dadosEmails = open(caminhoEmails, 'r')
for linha in dadosEmails:
    email = linha.strip()
    lista_emails.append(email)
    print(email)
dadosEmails.close()
    
print("\n-- Resultados --")
resultado = pagamentos.desafio(lista_compras, lista_emails)
for chave in resultado:
    print(chave,'pagará', resultado[chave], 'centavos')
