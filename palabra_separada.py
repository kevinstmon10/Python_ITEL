numeros = input("ingrese una serie de numeros: ")
numeros = numeros.split(",")
data = tuple(numeros)
count = len(data)
sum = 0

for i in data:
    sum = sum + int(i)
mean = sum/count
print(mean)