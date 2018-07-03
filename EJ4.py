"""

f = 32
temp = int((f - 32)*(5/9))

while temp < 73:
    print(f, temp )
    temp = temp + 1
    f = f + 1

"""

temp = 32
print("f°     c°")
while temp < 73:
    print(temp, "   ", int((temp-32)*5/9))
    temp = temp + 1