altura = float(input("Digite sua altura: "))
sexo = input("Digite m.masculino ou f.feminino: ")
if sexo=="m" or sexo=="M":
    peso =(72.7 * altura ) - 58
else: 
    peso=(62.1 * altura ) - 44.7
print("Seu peso ideal é ",round(peso))