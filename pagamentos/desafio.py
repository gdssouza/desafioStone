# Validação dos dados
def validaListas(listaCompras, listaEmails):
    if type(listaCompras) != list:
        return False, 'listaCompras não é uma lista.'
    elif type(listaEmails) != list:
        return False, 'listaEmails não é uma lista.'
    elif listaCompras == []:
        return False, 'A lista de compras está vazia.'
    elif listaEmails == []:
        return False, 'A lista de emails está vazia.'
    elif len(listaCompras) != 3:
        return False, 'A lista de compras não é 3xN'
    else:
        itens, qtds, precos = listaCompras
        if not( len(itens) == len(qtds) == len(precos)):
            return False, 'A lista de compras não é uma matriz'
        # Percorrendo cada elemento e verificando se há algum elemento com o tipo
        # de dado inválido
        for tipo in list(map(type, precos)):
            if tipo != float and tipo != int:
                return False, 'A lista de compras possui preços que não são números'
        if list(map(type, qtds)) != [int]*len(qtds):
            return False, 'A lista de compras possui pelo menos um produto com quantidade não inteira.'
        elif list(map(type, listaEmails)) != [str]*len(listaEmails):
            return False, 'A lista de emails não é completamente composta por strings'
        # Se tudo estiver ok, retorna True sem mensagem de erro
    return True, ''

# Calcula o valor total percorrendo a lista de compras
def retornaSoma(listaCompras):
    itens, qtds, precos = listaCompras
    soma = 0
    for i in range(0, len(itens)):
        soma += qtds[i]*precos[i]
    return soma
        
# Percorrendo a lista de emails e definindo os valores de pagamento
def fazMapa(soma_cents, listaEmails):
    sizeEmails = len(listaEmails)
    divisao_cents = soma_cents//sizeEmails
    restoDivisao_cents = soma_cents%sizeEmails
    mapa = {}
    for email in listaEmails[::-1]:
        mapa[email] = divisao_cents
        if restoDivisao_cents > 0:
            mapa[email] += 1
            restoDivisao_cents -= 1        
    return mapa
        
def desafio(listaCompras, listaEmails):
    '''
    Parameters
    ----------
    listaCompras : list of lists
        Matriz 3xN. Descrição das linhas:
            [0] Itens : str
            [1] Quantidade de cada item : int
            [2] Preço por unidade/peso/pacote de cada item em centavos: float
    listaEmails : list
        Lista com emails (str).

    Returns
    -------
    dict
        Chaves : e-mail
        Valores : valor a pagar
    '''
    result, msg = validaListas(listaCompras, listaEmails)
    if result == False:
        raise ValueError(msg)
    else:
        valorTotal = retornaSoma(listaCompras)
        mapa = fazMapa(valorTotal, listaEmails)
        return mapa
