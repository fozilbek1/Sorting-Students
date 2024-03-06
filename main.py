# Level 1

# students = ["Jerry", "Tom", "Sandy", "Spongebob", "Mr.Krabs"]
#
# # students.sort(reverse=True)
#
# sorted_students = sorted(students)
#
# for i in sorted_students:
#     print(i)


# Level 2

students = [("Jerry", "F", 60),
            ("Tom", "A", 33),
            ("Sandy", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78)]
age = lambda  ages:ages[2]
students.sort(key=age)

for i in students:
    print(i)
