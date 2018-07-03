# List sort

li = [9,1,8,2,7,3,6,4,5]
#li.sort()

s_li = sorted(li)
revSLi = sorted(li, reverse=True)


print(li)
print(s_li)
print(revSLi)

# Tuple sort

tup = (9,8,1,2,3,6,4,5,7,0)
s_tup = sorted(tup)
print(s_tup)


# Dictionaries sort

dic = {"nombre": "Aedel", "apellido": "Darko", "poder": "fuerza"}
sDic = sorted(dic)

print(sDic)

lis = [-6,-5,-4,-2,1,5,78,-100, 100]

absLis = sorted(lis, key=abs)
print(absLis)