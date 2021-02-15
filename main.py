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
        
def fazDivisao(soma, lista_emails):
    mapa = {}
    len_emails = len(lista_emails)
    soma_cents = soma*100
    divisao_cents = int(soma_cents/len_emails)
    
    for email in lista_emails:
        mapa[email] = divisao_cents
        
    if (len_emails%2 != 0) and (len_emails > 2):
        mapa[lista_emails[-1]] += soma_cents - divisao_cents*len_emails
        
    return mapa
        
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
        valor_total = retornaSoma(lista_compras)
        return fazDivisao(valor_total, lista_emails)

lista_compras = [ ['item']*100, [1]*100,[1]*100]
lista_emails = ['email1','email2','email3']
print(desafio(lista_compras, lista_emails))