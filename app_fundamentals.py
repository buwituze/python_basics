"""practice of different operators, if statements and a combination of both"""

## Operations and statements

## comparison operators: ==, !=, <, >, <=, >=

## If statements: if, elif, else

temperature = 28

if temperature > 30:
    print("It's a little hot, drink water!")
elif temperature > 20:
    print("Its nice and cozy weather")
else:
    print("It's a little cold, wear warm clothes!")
print("Done")

## ternary operator: <expression1> if <condition> else <expression2>

age = 18

status = "Adult" if age > 20 else "Child"
print(status)


## logical operators: and, or, not

defense = True
report = True
finance_standing = True

if defense and report:  ## or
    print("Graduate ready")
else:
    print("Graduate not ready")
print("complete")

# not--- this basically reverses the original boolean, true becomes false. and the if statement is skiped for falsy

if not defense:  
    print("NO graduation")
else:
    print("Graduation is possible")

    # combination of all 

if (defense or report) and not finance_standing:
    print("Graduation is possible")
else:
    print("Graduation is not possible")

## membership operators: in, not in

list = [1, 2, 3, 4, 5]
print(3 in list)

string = "Hello World"
print("H" not in string)

## identity operators: is, is not

x = 5
y = 3
print(x is y)

x = [1, 2, 3]
y = [1, 2, 3]
print(x is not y)

## chaining operators -- different ways

times = 5 

if times >= 0 and times < 6 :
    print("Times is between 0 and 5")

### these two are the same

if 0 <= times < 6 :
    print("Times is between 0 and 5")



