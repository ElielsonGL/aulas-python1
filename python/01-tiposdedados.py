#comentários de uma linha

''' comentários: auxiliam
a deixar
"anotações" no código fonte'''

#variavel é um espaço na memoria

# concatenação
print('Boas vindas a aula de' + ' Python!')

# interpolação
print ('Olá {}' . format(input('Qual o seu nome? ')))

# tipo de dados em python - números
# Inteiro (int) 1
idade = 30
print(idade)

# Decimal (float) 2
altura = 1.75
print(altura)

# Aula 2

# Número complexo 3 
numero_complexo = 2 + 3j
print(numero_complexo)

#texto(str) 4 (com " " o python entende que é um nome, não um numero)
nome = "Ana Cláudia"
print(nome)

#booleano(bool) 5
ativo = True
print(ativo)

logado = False
print(logado)

#nenhum valor (None type) 6
valor = None
print(valor)

#Lista(list) mutável 7 (mutável é quando pode mudar a lista)
frutas = ["maçã", "banana", "uva"]
print(frutas)

#tupla(tuple) imutável 8 (imutável é quando nao mode mudar a lista)
cores = ("vermelho", "azul", "verde")
print(cores)

#conjunto(set) 9 (lista para apenas NUMEROS)
numeros = {1, 2, 3, 4}
print(numeros)

#Dicionário(dict) pares chave-valor 10 
pessoa = {
    "nome": "Ana",
    "idade": 30
}
print(pessoa)


'''Python não tem constantes
verdadeiras, mas usamos uma convenção
para indicar que um valor não deve ser alterado.
 (escreva o nome da variavel em maiusculo para torna-lo constante)''' 
PI = 3.14159
GRAVIDADE = 9.8

print("O valor de PI é", PI , "\nO valor de Gravidade é" , GRAVIDADE)
# "\n" colocado para pular linha    n = New line