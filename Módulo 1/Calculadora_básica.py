#Calculadora básica de números inteiros
print("*************Calculadora*************")

while True:
    num1 = input("Digite um número: ")
    operador = input("Digite o operador: ")
    num2 = input("Digite outro número: ")

    #Checa se o que foi digitado é um número.
    if not num1.isnumeric() or not num2.isnumeric():
        print("Digite um número\n")
        continue

    #Converte as variáveis strings em floats.
    else:
        num1 = float(num1)
        num2 = float(num2)

    if operador == '+':
        print(f"Resultado: {num1 + num2}")

    elif operador == '*':
        print(f"Resultado: {num1 * num2}")

    elif operador == '-':
        print(f"Resultado: {num1 - num2}")

    elif operador == '/':
        print(f"Resultado: {num1 / num2}")

    else:
        print("Operador inválido")

    sair = input("Deseja sair? [s] ou [n]\n")

    if sair == 's':
        break