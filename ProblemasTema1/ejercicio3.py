def inserta_ordenado(lista :list, num :int) -> list:
    """ Devuelve la lista con el número insertado en orden ascendente """
    res = []
    if len(lista) == 0:
        res += [num]
    else:
        pos = 0
        while pos < len(lista) and lista[pos] < num:
            pos += 1
        if pos == len(lista):
            res = lista + [num]
        else:
            res = lista[:pos] + [num] + lista[pos:]
    return res

"""pares = []
impares = []
for num in lista:
    if num % 2 == 0:
        pares = inserta_ordenado(pares, num)
    else:
        impares = inserta_ordenado(impares, num)
print(pares)
print(impares)"""