"""practical exercises for strings and string methods """

print("Hello World!" + " Hello again")

students_count = 100
print(students_count)

### strings

course_name = "Python Study"

print(len(course_name))
print(course_name[0:4]) # to get the first 4 characters
print(course_name[:5])  # to get the first 5 characters
print(course_name[:])   # to get all characters

course_name = course_name.upper()
print(course_name)

course_name = course_name.lower()
print(course_name)

course_name = course_name.title() # to get the first letter of each word in uppercase
print(course_name)

course_name = course_name.strip()  ## to remove spaces, there is also lstrip (left strip) and rstrip (right strip)
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
