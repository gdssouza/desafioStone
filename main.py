def validaListas(lista_compras, lista_emails):
    if lista_compras == []:
        return False, 'A lista de compras está vazia.'
    elif lista_emails == []:
        return False, 'A lista de emails está vazia.'
    elif len(lista_compras) != len(lista_emails):
        return False, 'As listas não possuem o mesmo tamanho'
    else:
        return True, ''

def retornaSoma(lista_compras):
    itens, qtds, precos = lista_compras
    soma = 0
    for i in range(0, len(itens)):
        soma += qtds[i]*precos[i]
    return soma
        
def desafio(lista_compras, lista_emails):
    '''
    

    Parameters
    ----------
    lista_compras : list
        Matriz 3xN. Descrição das linhas:
            [0] Itens : str
            [1] Quantidade de cada item : int
            [2] Preço por unidade/peso/pacote de cada item em reais : int
    lista_emails : list
        Lista com emails (str).

    Returns
    -------
    dict
        Chaves : e-mail
        Valores : valor
        
    '''
    result, msg = validaListas(lista_compras, lista_emails)
    if result == False:
        return msg
    else:
        return {}

print(desafio([],[1]))
print(desafio([1],[]))
print(desafio([],[]))
print(desafio([0],[1,2]))