print("Fibonacci ou não")
valor_verifica = int(input("Digite um valor: "))

a = 1
b = 1

#for i in range(1, valor_verifica+1):
while True:
    c = a + b
    a = c
    if c > valor_verifica:
        print(f"{valor_verifica} NÃO está na Sequencia de Fibonacci")
        break
    if c == valor_verifica:
        print(f"{valor_verifica} está na Sequencia de Fibonacci")
        break

    d = a + b
    b = d
    if d > valor_verifica:
        print(f"{valor_verifica} NÃO está na Sequencia de Fibonacci")
        break
    if d == valor_verifica:
        print(f"{valor_verifica} está na Sequencia de Fibonacci")
        break


