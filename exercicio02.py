import math 
n1=int(input("insira o primeiro numero"))
n2=int(input("insira o segundo numero"))
print("Digite 1. potencia, 2.raiz quadrada, 3.raiz cúbica")
opcao=int(input())
if opcao=="1":
        print("Potencia ", pow(n1,n2))
elif opcao==2:
        print("Raiz quadrada de ",n1 ," é ", math.sqrt(n1))
        print("Raiz quadrada de ",n2 ," é ", math.sqrt(n2))
elif opcao==3:
        print("Raiz cúbica de ",n1 ," é ", pow(n1, 1/3))
        print("Raiz cúbica de ",n2 ," é ", pow(n2, 1/3))