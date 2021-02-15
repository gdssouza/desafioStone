# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15

@author: Gustavo
"""

# Validação dos dados
def validaListas(lista_compras, lista_emails):
    itens, qtds, precos = lista_compras
    if lista_compras == []:
        return False, 'A lista de compras está vazia.'
    elif lista_emails == []:
        return False, 'A lista de emails está vazia.'
    elif len(lista_compras) != 3:
        return False, 'A lista de compras não é 3xN'
    elif not( len(itens) == len(qtds) == len(precos)):
        return False, 'A lista de compras não é uma matriz'
    
    # Percorrendo cada elemento e verificando se há algum elemento com o tipo
    # de dado inválido
    for tipo in list(map(type, precos)):
        if tipo != float and tipo != int:
            return False, 'A lista de compras possui preços que não são números'
    if list(map(type, qtds)) != [int]*len(qtds):
        return False, 'A lista de compras possui pelo menos um produto com quantidade não inteira.'
    elif list(map(type, lista_emails)) != [str]*len(lista_emails):
        return False, 'A lista de emails não é completamente composta por strings'
    
    # Se tudo estiver ok, retorna True sem mensagem de erro
    return True, ''

# Calcula o valor total percorrendo a lista de compras
def retornaSoma(lista_compras):
    itens, qtds, precos = lista_compras
    soma = 0
    for i in range(0, len(itens)):
        soma += qtds[i]*precos[i]
    return soma
        
# Percorrendo a lista de emails e definindo os valores de pagamento
def fazDivisao(soma, lista_emails):
    mapa = {}
    sizeEmails = len(lista_emails)
    soma_cents = soma*100
    divisao_cents = int(soma_cents/sizeEmails)
    restoDivisao_cents = soma_cents%sizeEmails
    
    for email in lista_emails[::-1]:
        mapa[email] = divisao_cents
        if restoDivisao_cents >= 1:
            mapa[email] += 1
            restoDivisao_cents -= 1        
    return mapa
        
class Desafio:
    '''
    

    Parameters
    ----------
    lista_compras : list
        Matriz 3xN. Descrição das linhas:
            [0] Itens : str
            [1] Quantidade de cada item : int
            [2] Preço por unidade/peso/pacote de cada item em reais : float
    lista_emails : list
        Lista com emails (str).

    '''
    def __init__(self, lista_compras, lista_emails):
        result, msg = validaListas(lista_compras, lista_emails)
        if result == False:
            raise ValueError(msg)
        self.listaCompras_ = lista_compras
        self.listaEmails_ = lista_emails
        
    # Função que responde o teste técnico
    def retornaMapa(self):
        '''
        

        Returns
        -------
        dict
            Chaves : e-mail
            Valores : valor a pagar

        '''
        self.valorTotal_ = retornaSoma(self.listaCompras_)
        return fazDivisao(self.valorTotal_, self.listaEmails_)
    
    def get_valorTotal(self):
        return self.valorTotal_