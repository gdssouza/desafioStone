# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15

@author: Gustavo
"""

import pagamentos

def testar(caminhoCompras, caminhoEmails):
    lista_compras = [[], [], [] ]
    with open(caminhoCompras, 'r') as dadosCompras:
        for linha in dadosCompras:
            item, qtd, preco = linha.strip().split(',')
            qtd, preco = int(qtd), float(preco)
            lista_compras[0].append(item)
            lista_compras[1].append(qtd)
            lista_compras[2].append(preco)

    lista_emails = []
    with open(caminhoEmails, 'r') as dadosEmails:
        for email in dadosEmails:
            lista_emails.append(email.strip())
            #print(email)
        
    resultado = pagamentos.desafio(lista_compras, lista_emails)
    print(resultado)

if __name__ == '__main__':
    import sys
    caminho_compras = sys.argv[1]   # exemplo <- dados/datasetCompras_exemplo.csv
    caminho_emails = sys.argv[2]    # exemplo <- dados/datasetEmails_exemplo.csv
    testar(caminho_compras, caminho_emails)