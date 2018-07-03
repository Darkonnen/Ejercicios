from Ej9 import find_index, test
import sys

sys.path.append("Users\\Adel Cabrera\\Desktop\\Personal")

courses = ["History", "Math", "Art", "CompSci"]

index = find_index(courses, "Math")
print(index)
print(test)
print(sys.path)
print("hola")

v1 = "primera string"
v2 = "segunda string"

temp = v1
v1 = v2
v2 = temp

print(v1)
print(v2)
