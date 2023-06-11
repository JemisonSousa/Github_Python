# modo limidado de argumento
# def somar(n1, n2):
#     soma = n1 + n2
#     print("A soma é " + str(soma))

# somar(2,6)
# somar(5, 69)

# Modo ilimitado de argumento
def somar(*num):
    r = 0
    for n in num:
        r += n

    print("A soma é = " + str(r))

somar(2,3, 58, 548, 8.5)
