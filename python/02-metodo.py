#calculos 1
#input capta a digitação (escrever algo)
#int converte o resultado e deixa o numero inteiro para uma soma por exemplo.
num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

soma = int(num1) + int(num2)
subtracao = int(num1) - int(num2)
divisao = int(num1) / int(num2)
moduloresto = int(num1) % int(num2)
multiplicacao = int(num1) * int(num2)
potenciacao = int(num1) ** int(num2)

print(soma)
print(subtracao)
print(divisao)
print(moduloresto)
print(multiplicacao)
print(potenciacao)

#type serve para descobrir o tipo de dado que esta armazenado
# o comando type retorna o tipo da variável
print(type(num1))
print(type(soma))

#Calcular área
lado1 = input('Informe o primeiro lado: ')
lado2 = input('Informe o segundo lado: ')

area = float(lado1) * float(lado2)

print('A area do quadrado é: {} '. format(area))

nomecompleto =  input('Informe o seu nome completo: ')
# função len retorno a quantidade de caracteres de uma variável
print('1. Quantidade de caracteres:', len(nomecompleto))

#len conta a quantidade de caracteres ( ) espaço tbm é contado.
#upper =  transforma um texto em maiusculo
#lower = transforma um texto em minusculo
# capitalize =  somente a primeira letra em maiusculo
print('2. Nome em maiusculo:', nomecompleto.upper())
print('3. Nome em minusculo:', nomecompleto.lower())
print('4. Primeira letra em maiusculo:', nomecompleto.capitalize())

