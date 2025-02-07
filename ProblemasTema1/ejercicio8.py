#EJERCICIO 8
def invertir(n):
    def inverso(n, acc):
        if n == 0:
            return acc
        else:
            return inverso(n // 10, acc * 10 + n % 10)
    return inverso(n, 0)

print(invertir(726))   