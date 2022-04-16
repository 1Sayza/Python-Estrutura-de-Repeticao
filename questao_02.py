sair = "sim"
Qtvogais = 0
while sair.lower() == "sim":
   string = input("Digite um nome:")
   i = 0
   if string[i] == "a":
     Qtvogais += 1
     i+=1
   sair = input("Deseja continuar no programa? [sim/nao]:")
print("Total de vocais são: {}" .format(Qtvogais))
print("Fim do programa. ")