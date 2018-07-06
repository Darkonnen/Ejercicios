"""
n = 100


for i in range(1, n+1):
    if i % 2 == 0 or i % 3 == 0 and i != 3 or i%5 ==0 and i!=5 or i%7 ==0 and i%7 != 7:
        print(i, "even")
    else:
        print(i, "odd")
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(sorted(list(set(i for i in a+b))))