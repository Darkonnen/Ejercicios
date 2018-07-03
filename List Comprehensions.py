# List comprehensions

nums = [1,1,1,2,3,3,3,4,5,5,5,6,7,8,9,10]
numbs = [1,2,3,4,5,6,7,8,9,10]

my_list = []
for n in nums:
    my_list.append(n)

myList = [n for n in nums]

print(my_list)
print(myList)

mymult = []
for n in nums:
    mymult.append(n*n)                # 1 forma

myMult = [n*n for n in nums]          # 2 forma

myLambda = list(map(lambda n: n*n, nums)) # 3 forma

print(mymult)
print(myMult)
print(myLambda)

myeven = []
for n in nums:
    if n%2 == 0:
        myeven.append(n)

myEven = [n for n in nums if n%2 == 0]
myEven2 = list(filter(lambda n: n % 2 == 0, nums))

print(myeven)
print(myEven)
print(myEven2)

myletternumpair = []
for letter in "abdc":
    for num in range(4):
        myletternumpair.append((letter, num))


myLetterNumPair = [(letter, num) for letter in "abcd" for num in range(4)]

print(myletternumpair)
print(myLetterNumPair)



# Dictionaries comprehensions

names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heroes = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]

my_dict = {}
for name, hero in zip(names, heroes):
    my_dict[name] = hero

myDict = {name: hero for name, hero in zip(names, heroes) if name != "Peter"}

print(my_dict)
print(myDict)


# Set Comprehensions

my_set = set()
for n in nums:
    my_set.add(n)

mySet = {n for n in nums}

print(my_set)
print(mySet)


# Generators

def gen_func(numbs):
    for n in numbs:
        yield n*n

my_gen = gen_func(numbs)

myGen = (n*n for n in nums)

for i in my_gen:
    print(i)

for n in myGen:
    print(n)

