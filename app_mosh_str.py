""" THIS IS A BUNCH OF PRACTICE CODE FOR PYTHON """

# print("Hello World!" + " Hello again")
students_count = 100
print(students_count)

### strings

course_name = "Python Study"

print(len(course_name))
print(course_name[0:4])
print(course_name[:5])
print(course_name[:])

course_name = course_name.upper()
print(course_name)

course_name = course_name.lower()
print(course_name)

course_name = course_name.title()
print(course_name)

course_name = course_name.strip()  ## there is also lstrip and rstrip
print(course_name)

# course_name = course_name.find("thon")
# print("Thon is at: " + str(course_name))

course_name = course_name.replace("python" , "Java")
print(course_name)

print("tudy" in course_name) 

print("python" not in course_name)

### concantinating

month  = "First month is \'January\'"
print(month)

first_name = "Benitha"
middle_name = "Uwituze"

full_name = f"{first_name} {middle_name}"
print(full_name)




