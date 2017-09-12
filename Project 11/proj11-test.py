##################################
#     
#   Project 11 Test
# 
#     This program serves as a test bed to demonstrate  that the implementation 
#       of the classes created are correct. 
#     
# 
#################################

#  Demonstrate all methods (except __repr__ which can only be demonstrated in the Python shell)
#  Include print statements so your output can be read and understood without reading the code

import classes

print("Create a Grade instance: p01, 75, .8")
g1 = classes.Grade("p01",75,.8)    # tests __init__
print("Print the Grade instance")
print(g1)        # tests __str__


# Create a Student instance, let's call it s1
# Then print s1, include descriptive print statements such as above
# Demonstrate add_grade and calculate_grade
# Create another student instance
# Demonstrate comparison operators 
print()

g2 = classes.Grade("p02", 87, .9)
g3 = classes.Grade("p03", 89, .8)
g4 = classes.Grade("p04", 92, .8)
#create more grades to then demonstrate the add_grade function works properly

grade_list = [g1]
print("Create Student one instance: Mary, Smith, 223")
s1 = classes.Student(223,'Mary', 'Smith',  grade_list)
print("Print Student one instance")
print(s1)
#prints what student one is 
print()
print("Add grade to student one")
s1.add_grade(g2)
print (s1)
#adds a grade to student one and then prints the updated grade.
print()

print("Create Student two instance: Tom, Rose, 423")
s2 = classes.Student( 423,'Tom', 'Rose', grade_list)
#prints what student two is
print("Print Student two instance")
print(s2)

print()
print("Add grade to student two")
s2.add_grade(g3)
print(s2)
print()
#adds a grade to student two and then prints the updated grades.




print()
print("Operator comparison of s1 and s2")
print("s1 > s2: ", end = "")
print(s1>s2)
#checks if student one is greater than student two

print("s1 == s2: ", end = "")
print(s1==s2)
#checks if student one is equal to student two

print("s1 < s2: ", end = "")
print(s1 < s2)
#checks if student one is less than student two