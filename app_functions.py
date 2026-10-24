"""practice for functions"""


def day():
    print("It's Monday!")

day()



## Arguments:

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")



# There are two types of functions:
## 1. perform a task (e.g.: print(), greet() above )
## 2. return a value (e.g.: round(4.5))

def get_day(name):
    return f"Today is {name}."

message = get_day("Tuesday")
print(message)


## creating and printing to a file
file = open("my_file.txt","w")
file.write(message)
file.close()



# multiple arguments
def friendly_greet(name, day_name):
    return f"Hello, {name}! Today is {day_name}."

print(friendly_greet("Alice", "Wednesday"))


def increment(num, by): 
    return num + by

output = increment(5,2)
print(output)

            # similarly this function can be called like this:
# print(increment(5, by=2))
# print(increment(5, 2))



# def increment(num, by=1):  # we can make a default argument
#     return num + by

# output = increment(5,2)  # if there is a default argument, it can be skipped and the default value will be used
# print(output)



# Exercise: multiplying tuple items (functions and loops)

def multiply(*nums):
    product = 1

    for i in nums:
        product *= i
        # print(product)
    return product

result = multiply(1, 2, 3, 4, 5)
print(result)
