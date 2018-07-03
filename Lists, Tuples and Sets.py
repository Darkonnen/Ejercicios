courses = ["History", "Math", "Chemistry", "CompSci"]
degree = ["Psychology", "Neuroscience", "Medicine", "Physics"]
grades = [1, 2, 3, 4, 3, 6, 5]

print(courses[0])
print(courses[0: 2])
courses[1] = "Art"
courses.append("Language")
courses.insert(3, "Sports")
courses.extend(degree)
courses.sort()
courses.remove("Medicine")
courses.pop()
courses.reverse()
var = sorted(courses)
course_str = ','.join(courses)
new_list = course_str.split(',')
print(course_str)
print(new_list)
print("Psychology" in courses)
print(courses.index("Neuroscience"))
print(courses)
print(degree)
print(var)
print(min(grades))
print(max(grades))
print(sum(grades))

for index, course in enumerate(courses, start=1):
    print(index, course)

# sets no tienen orden, remueve valores duplicados

cs_courses = {"History", "Math", "Physics", "CompSci", "Math"}
art_courses = {"History", "Math", "Art", "Design", "Math"}

print("Math" in cs_courses)

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))



