n=int(input("Digite um número "))
if not n % 4 != 0 and n % 7==0:
	print(n, "é múltiplo de 4 e 7")
else:
	print(n, "não é múltiplo de 4 e 7")