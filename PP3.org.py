a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []

answ = int(input("Ingresa un número > "))

for i in a:
    if i < answ:
        b.append(i)

print(b)

