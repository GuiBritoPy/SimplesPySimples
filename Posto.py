# -*- coding: utf-8 -*-
"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3%.
acima de 20 litros, desconto de 5%.
Gasolina:
até 20 litros, desconto de 4%.
acima de 20 litros, desconto de 6%. Escreva um algoritmo que leia o
número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do
litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

""" 
#Preços
gas = 2.50
alc = 1.90

#Entrada do usúario de litros
litros = int(input("Quer abastecer quantos litros? "))

#Preços que o Consumidor irá pagar
lg = gas * litros
la = alc * litros

#Descontos
descA1 = la * (3/100)
descA2 = la * (5/100)
descG1 = lg * (4/100)
descG2 = lg * (6/100)


#Print dos preços
print ("Valor com Gasolina (R$ 2.50) = %.2f" %(lg))
print ("Valor com Álcool (R$ 1.90) = %.2f" %(la))

#Usuário escolhe de que forma quer abastecer
esc = str(input("Você quer abastecer com Álcool ou Gasolina? Digite A para Álcool e G para Gasolina: ")).upper()


#Condições se ele escolher álcool
if esc == "A":
    print("===============================")
    print("Então você abastecerá com álcool!")
    print("===============================")
    print("Você pagaria sem desconto: %.2f."%(la))
    if litros <= 20:
        print("Você pagará com desconto R$%.2f" %(la - descA1))
    elif litros > 20:
        print("Você pagará com desconto R$%.2f" %(la - descA2))

#Condĩções e descontos se escolher gasolina
if esc == "G":
    print("===============================")
    print("Então você abastecerá gasolina!")
    print("===============================")

    print("Você pagaria sem desconto: %.2f."%(lg))
    if litros <= 20:
        print("Você pagará com desconto R$%.2f" %(lg - descG1))
    elif litros > 20:
        print("Você pagará com desconto R$%.2f" %(lg - descG2))

if esc != "G":
    if esc != "A":
        print("Você digitou uma letra inválida")
