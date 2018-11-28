lista=[1,2,3,"quatro",5,6,7]
print(lista)
lista.append("oito")
print(lista)
# o 3 aqui é integer, não string
print("O número 3 está na lista?",3 in lista)
print("Qual a posição do número 7 na lista?",lista.index(7))
print("Quantas vezes tem o número 4 na lista?",lista.count(4))
print("Adicionar o número 4 na lista")
lista.append(4)
print("E agora?",lista.count(4))
print("Remove a string 'oito' da lista")
lista.remove("oito")
print(lista)
