sair = "sim"
listanomes = []
conta_letra = 0
while sair.lower() == "sim":
   x = input("Digite um nome:")
   conta_letra = conta_letra +1
   listanomes.append(x)
   
   if x in "aiou":
     print(listanomes)
   sair = input("Deseja continuar no programa? [sim/nao]:")
print( "Total de nomes: {}" .format(len(listanomes)))
print("Fim do programa. ")