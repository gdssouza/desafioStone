def validaListas(lista_compras, lista_emails):
    if lista_compras == []:
        return False, 'A lista de compras está vazia.'
    elif lista_emails == []:
        return False, 'A lista de emails está vazia.'
    elif len(lista_compras) != len(lista_emails):
        return False, 'As listas não possuem o mesmo tamanho'
    else:
        return True, ''

def desafio(lista_compras, lista_emails):
    result, msg = validaListas(lista_compras, lista_emails)
    if result == False:
        return msg
    else:
        return {}

print(desafio([],[1]))
print(desafio([1],[]))
print(desafio([],[]))
print(desafio([0],[1,2]))