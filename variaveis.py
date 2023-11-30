nome = "jose"
numero = 6
troco = 4.65
is_login = True # sempre com a primeira letra maiuscula
print(type(nome))
print(type(numero))
print(type(troco))
print(type(is_login))

nomes = ["Maria", "João", "Fábio","Ana", "Zé"]
print(type(nomes)) #Mostrar o tipo List
print(nomes) #Mostra a lista 
#print (nomes[1]) #Mostra a posição 2
print(nomes.pop()) #Exclui a ultima posição mostra o nome 
print(nomes) #Mostra a lista novamente 
nomes.pop() #Exclui a ultima posição
print(nomes)
nomes.append("Ana") #Adiciona um nome no final da lista
nomes.append("Lorenzo")
print(nomes)


forx in nomes:
print(x)
