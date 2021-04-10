#Par ou Ímpar
num = float(input("Digite um número inteiro: "))

#Checa se o número digitado é inteiro
if num % 1 != 0:
    print("O número digitado não é inteiro.")

#Checagem par ou ímpar
else:
    if num % 2 == 0:
        print("O número digitado é par")

    else:
        print("O número digitado é ímpar")