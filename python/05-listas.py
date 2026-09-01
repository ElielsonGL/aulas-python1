frutas = ["maçã", "banana", "uva"]
print(frutas)

#ver o primeiro elemento da lista    ( index = posição   ex: [0], [1] etc)
print(frutas[0])

#retornando demais elementos no seu index
print(frutas[1])
print(frutas[2])

#modificando
frutas[1] = "laranja"
print(frutas)

#adicionando itens no final da lista
frutas.append("pêra")
print(frutas)

#adicionar no começo da lista
frutas.insert(0, "abacaxi")
print(frutas)

#procurando, como encontrar um produto em uma lista (posição do item)
indice =  frutas.index("uva")
print(indice)

if "uva" in frutas:
    print("Uva está na lista!")

#removendo itens de uma lista.
frutas.remove("uva")
print(frutas)

if "uva" in frutas:
    print("Uva está na lista!")
else:
    print("Uva foi removido da lista!")

#tamanho da lista  ~ #len para saber quantos itens tem na lista
numeros = [100, 28, 4, 31]
print(len(numeros))

#ordenar  A-Z ou se for numeros fica em forma crescentes.
numeros.sort()
print(numeros)

frutas.sort()
print(frutas)

#inverter ~ deixar lista em forma decrecente
numeros.reverse()
print(numeros)

frutas.reverse()
print(frutas)

#verificar se existe na lista
print(2 in numeros)
print(100 in numeros)

#adicionando varios elementos em uma lista ao mesmo tempo
numeros = [10, 20, 30] + numeros
#ordenei
numeros.sort()
print(numeros)

#percorrer com for
for n in numeros:
    print(n)

print(type(n))
print(type(numeros))
