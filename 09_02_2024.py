# -*- coding: utf-8 -*-
"""09/02/2024.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Aelvdq9Qylnbj6iIuHHX3HLo7b3O7EY8
"""

idade = int(input("Digite sua idade: "))

if idade >=0 and idade <=11:
  print("Criança")

elif idade >=12 and idade <=18:
  print("Adolescente")

elif idade >=19 and idade <=24:
  print("Jovem")

elif idade >=25 and idade <=40:
  print("Adulto")

elif idade >=41 and idade <=60:
  print("Meia idade")

else:
  print("Idoso")

salario = int(input("Digite o seu salário: "))
reajuste = 0
percentual = 0
newsalario = 0

if salario <=280 :
  percentual = 20

elif salario > 280 and salario <= 700:
  percentual = 15

elif salario > 700 and salario <= 1500:
  percentual = 10

else:
  percentual = 5

reajuste = salario * percentual / 100
newsalario = salario + reajuste

print(f"O valor do seu salário é {salario}, o percentual do seu reajuste é de {percentual}% o valor do seu aumento é de {reajuste}, e o seu novo salário é de {newsalario}.")

numero = int(input("Coloque um número de 1 a 7: "))

if numero == 1:
  print("Hoje é dia 1, Domingo.")

elif numero == 2:
  print("Hoje é dia 2, Segunda-feira.")

elif numero == 3:
  print("Hoje é dia 3, Terça-feira.")

elif numero == 4:
  print("Hoje é dia 4, Quarta-feira.")

elif numero == 5:
  print("Hoje é dia 5, Quinta-feira.")

elif numero == 6:
  print("Hoje é dia 6, Sexta-feira.")

elif numero == 7:
  print("Hoje é dia 7, Sábado.")

else:
  print("valor inválido.")

opcao = int(input("Insira 1 para converter Celsius para Fahrenheit e insira 2 para o contrário: "))
celsius = 0
fahrenheit = 0
resultado = 0

if opcao == 1:
   celsius = int(input("Digite o valor da temperatura em Celsius: "))
   resultado = celsius * 1.8 + 32
   print(resultado)

elif opcao == 2:
  fahrenheit = int(input ("Digite o valor da temperatura em Fahrenheit: "))
  resultado = (fahrenheit - 32) / 1.8
  print(resultado)

else:
  print("Valor inválido")

idade = int(input("Insira sua idade: "))

if idade <16:
  print("Proibido de votar.")

elif idade >= 16 and idade <= 18:
  print("Optativo para votar.")

elif idade >= 18 and idade <= 65:
  print("Obrigatório de votar.")

elif idade >= 65:
  print("Optativo para votar. ")

print("Responda às seguinte perguntas como sim ou não:")
pergunta1 = input("Telefonou para a vitima?").lower()
pergunta2 = input("Esteve no local do crime?").lower()
pergunta3 = input("Mora perto da vitima?").lower()
pergunta4 = input("Devia para a vitima?").lower()
pergunta5 = input("Já trabalhou com a vitima?").lower()

positivas = 0

if pergunta1 == "sim":
  positivas += 1
if pergunta2 == "sim":
  positivas += 1
if pergunta3 == "sim":
  positivas += 1
if pergunta4 == "sim":
  positivas += 1
if pergunta5 == "sim":
  positivas += 1

if positivas == 2:
  print("Suspeita")
# elif 3 <= positivas <= 4:
elif positivas >=3 and positivas <=4:
  print("Cumplice")
elif positivas == 5:
  print("bandindinho")
else:
  print("inocente")