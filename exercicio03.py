n1,n2,n3 = (map(int,input("insira tres numeros: ").split()))
par = 0
impar = 0
if n1 % 2 == 0:
    print ("o primeiro número é par")
    par =par + 1
elif n1 % 2 != 0:
    print ("o primeiro número é ímpar")
    impar = impar + 1
if n2 % 2 == 0:
    print ("o segundo número é par")
    par = par + 1
elif n2 % 2 != 0:
    print ("o segundo número é ímpar")
    impar = impar + 1
if n3 % 2 == 0:
    print ("o terceiro número é par")
    par = par + 1
elif n3 % 2 != 0:
    print ("o terceiro número é ímpar")
    impar = impar + 1
print ("o total de pares",par)
print ("o total de ímpares",impar)