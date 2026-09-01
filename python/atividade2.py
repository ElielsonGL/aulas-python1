# Atividade 2 
# Exercicio 1 ~ Manicure
manicure_simples = float(30.00)

nome = input('Nome cliente:')
quantidade_unhas = float(input('Quantas unhas foram decoradas?:'))
print(nome.upper())
print('Valor total a pagar:' , manicure_simples + float(quantidade_unhas) * 2.0 , 'R$')
print ('Quantidade de caracteres do nome:' , len(nome))

# Exercicio 2 ~ Lava jato
simples = (25.0)
completa = (50.0)

nome =  input('Qual o nome do cliente?:')
escolha = input('O cliente escolheu a lavagem simples ou completa?:')

if escolha == 'simples':
    print('O serviço escolhido foi a lavagem simples, valor a pagar:' , float(simples) , 'R$')
elif escolha == 'completa':
    print('O serviço escolhido foi a lavagem completa, valor a pagar:' , float(completa) , 'R$')
else:
    print('Não temos esse serviço disponivel, escolha entre lavagem completa ou simples.')

# Exercicio 3  ~ Estacionamento pago.
hora = (5.0)
desconto = (10.0)
nome = input('Qual o nome do motorista?:')
quantidade_hora = float(input('Qual quantidade de horas estacionadas?:'))
valor_total = ((hora) * (quantidade_hora))  

if valor_total > 30:
    print('O cliente recebeu um desconto de 10% por exceder o valor de 30.00 R$')
else:
    print('O valor total a pagar é:' , valor_total )
#exercicio incompleto, falta calcular porcetagem de 10%

#Exercicio 4 ~ Escola Infantil

nome_crianca = input('Qual o nome da criança?:')
idade_crianca = int(input('Qual idade da criança?'))

if idade_crianca == 4:
    print("Maternal")
elif idade_crianca == 6:
    print('Jardim')
elif idade_crianca == 8:
    print('Pré escola')
else:
    print('Fora da faixa atendida')
# Não consigo deixar duas ou mais opçoes no if e else;
print(nome_crianca.upper())
print(nome_crianca.lower())
print('Quantidade de caracteres do nome:', len(nome_crianca))

#Exercicio 5 Pastelaria

pastel_queijo = float(8.00) 
pastel_carne = float(9.00)