# Sorting-Students
Level 1
Description:

The script sorts a list of student names alphabetically and prints them in ascending order.
Code:

python

students = ["Jerry", "Tom", "Sandy", "Spongebob", "Mr.Krabs"]

sorted_students = sorted(students)

for student in sorted_students:
    print(student)

Level 2
Description:

The script sorts a list of student tuples based on their age and prints them in ascending order of age.
Code:

python

students = [("Jerry", "F", 60),
            ("Tom", "A", 33),
            ("Sandy", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78)]

# Define a lambda function to extract age from each tuple
age = lambda student: student[2]

# Sort students based on age using the defined lambda function
students.sort(key=age)

# Print sorted students
for student in students:
    print(student)

Note:

In Level 2, the sort method is used with a key argument to sort the students list based on the third element (age) of each tuple. The lambda function age is provided as the key to extract the age from each tuple for sorting purposes.
