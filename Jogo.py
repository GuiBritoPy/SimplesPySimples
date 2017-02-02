# -*- coding: utf-8 -*-
'''

Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". 

    '''

while True:
    ok = "Ok, vamos continuar"
    nome = str(input("Olá, qual o seu nome? "))
    idade = str(input("Quantos anos você tem? "))
    sexo = str(input("Qual o seu sexo? (M - Masculino e S - Feminino) ")).upper()
    if sexo == "F":
        sexo = Feminino
    if sexo == "S":
        sexo = Masculino
    ch = 0
    print("Ok, vamos começar")
    p1 = str(input("Telefonou para a vítima? (S - Sim e N - Não) ")).upper()
    if p1 != "S" and p1 != "N":
        print("Entrada Inválida")
    elif p1 == "S":
        ch += 1
        print(ok)
    else:
        ch += 0
        print(ok)
    p2 = str(input("Esteve no local do crime? (S - Sim e N - Não) ")).upper()
    if p2 != "S" and p2 != "N":
        print("Entrada Inválida")
    elif p2 == "S":
        ch += 1
        print(ok)
    else:
        ch += 0
        print(ok)
    p3 = str(input("Mora perto da vítima? (S - Sim e N - Não) ")).upper()
    if p3 != "S" and p3 != "N":
        print("Entrada Inválida")
    elif p3 == "S":
        ch += 1
        print(ok)
    else:
        ch += 0
        print(ok)
    p4 = str(input("Devia para a vítima? (S - Sim e N - Não) ")).upper()
    if p4 != "S" and p4 != "N":
        print("Entrada Inválida")
    elif p4 == "S":
        ch += 1
        print(ok)
    else:
        ch += 0
        print(ok)
    p5 = str(input("Já trabalhou para a vítima? (S - Sim e N - Não) ")).upper()
    if p5 != "S" and p5 != "N":
        print("Entrada Inválida")
    elif p5 == "S":
        ch += 1
        print("Ok")
    else:
        ch += 0
        print ("Ok")
    #2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
    print ("#*"*10)
    print("Vamos ao relatório")
    print ("#*"*10)
    if ch == 2:
        print("{} de {} anos do sexo {} é considerado(a) Suspeito(a)".format(nome,idade))
    elif 2 < ch <= 4:
        print("{} de {} anos do sexo {} é considerado(a) Cúmplice.".format(nome,idade))
    elif ch == 5:
        print("{} de {} anos do sexo {} é considerado(a) Assassino(a) do crime.".format(nome,idade))
    else:
        print("{} de {} anos do sexo {} é considerado(a) Inocente.".format(nome,idade))

    print("Próxima Pessoa")
    

    
