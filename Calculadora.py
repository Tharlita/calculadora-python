print ("CALCULADORA DA HANNA")

# O while true diz "repita isso sempre até eu mandar parar"

while True:
    print("Escolha uma opração:")
    print("1 - Somar")
    print("2 - Subtrair")    
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")
    opçao = input("Digite a opção: ")

# o == significa comparação e o if significa SE

    if opçao == "5":
        print ("Encerrando a calculadora... Até mais!")
        break

# o in significa "está dentro de..." e aí vem a lista de valores

    if opçao in ["1", "2", "3", "4",]:

# tudo que vem do input é texto, então aqui tive que converter para número decimal usando float

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    if opçao == "1":
        resultado = num1 + num2
        print(f"Resultado: {resultado}")

# o elif é como "se não for a condição anterior, mas essa aqui for verdadeira, faça isso..."

    elif opçao == "2":
        resultado = num1 - num2
        print(f"Resultado: {resultado}")
    elif opçao == "3":
        resultado = num1 * num2
        print(f"Resultado: {resultado}")
    elif opçao == "4":
        if num2 == 0:
            print("Erro: não é possível dividir por zero!")
        else:
            resultado = num1 / num2
            print(f"Resultado: {resultado}")
    else:
            print("Opção inválida! Tente novamente.")