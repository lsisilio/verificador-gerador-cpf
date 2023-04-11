from random import randint


def calcular_digito(multiplicacao, corpo):
    #Cálculo seguindo o algoritmo
    calculo = 0
    for i, j in zip(multiplicacao, corpo):
        calculo += i * int(j)
    resto = calculo % 11
    return 0 if resto < 2 else 11 - resto


def descobrir_digitos(cpf):
    #Separar o corpo dos verificadores
    corpo = cpf[:9]
    digitos = cpf[-2:]
    #Valores de multiplicação no algoritmo
    multiplicacao = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    #Calculando primeiro dígito
    digito_1 = calcular_digito(multiplicacao, corpo)
    #Calculando segundo dígito
    corpo += str(digito_1)
    digito_2 = calcular_digito(multiplicacao, corpo[1:])
    #Converte em string e retorna
    digitos = str(digito_1) + str(digito_2)
    return digitos


def verificar(cpf_recebido):
    cpf = list(cpf_recebido)
    #Evitar inexistentes que seriam válidos
    lista_invalidos = [
            '11111111111', '22222222222', '33333333333',
            '44444444444', '55555555555', '66666666666', 
            '77777777777', '88888888888', '99999999999', 
            '00000000000']
    #Mais verificações
    if cpf_recebido.isnumeric():
        if cpf_recebido not in lista_invalidos: 
            if len(cpf) == 11:
                #Gerar os dígitos corretos
                digitos = descobrir_digitos(cpf)
                print(f"\n\tDígitos V.:{digitos}")
                print(f"\tCPF: {cpf_recebido}")
                #Comparar com os dados obtidos
                if (cpf[9] == digitos[0]) and (cpf[10] == digitos[1]):
                    print("\tCPF válido!")
                else:
                    print("\tCPF inválido!")
            else:
                print("\tCPF deve conter 11 dígitos")
        else:
            print("\tCPF não pode ter números iguais")
    else:
        print("\tCPF deve ser um número")


while True:
    #Menu
    cpf_recebido = input(
            "\nDigite o cpf,\n'x' para sair ou\n'c' para gerar um cpf válido\n")
    #Opção SAIR
    if cpf_recebido.lower() == 'x':
        print("Encerrado")
        break
    #Opção GERAR
    elif cpf_recebido.lower() == 'c':
        #Cria uma lista com 9 números randomicos
        cpf_criado = []
        for i in range(9):
            cpf_criado.append(randint(0,9))
        #Utilizando o algoritmo, cria os dois finais
        x = descobrir_digitos(cpf_criado)
        cpf_criado.append(x)
        #Converte em string e printa
        string_cpf = ''.join(str(e) for e in cpf_criado)
        print(f"\tCPF válido gerado: {string_cpf}")
    #Opção VERIFICAR
    else:
        verificar(cpf_recebido)