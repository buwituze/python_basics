"""practical exercises with different types of loops and iterable data types"""

# For loops: use this when you know how many times you want to loop through a block of code.

for num in range(4):
    print("Number:" , num)

for num in range(4 , 10):  ## this says: from this number to this (4,5)
    print("Number is", num, num + 2)

for num in range(1, 14, 3):  ## this handles additions automatically, the last number says skip these spots to the next number within the range
    print("Number with steps is", num)



## For... Else loop : Use For loop combined with else to perform an action conditionally

success = False

for count in range(4):
    print("Sent message")
    if success:
        print("Done. Successful")
        break
else:
    print("Failed. Not successful")



### Nested loops

for x in range(3):
    for y in range(3):
        print(f"{x} , {y}")



## Iterables: list, tuple, dictionary, set, range, string. 

for x in "Python":
    print(x)

for n in [1,2,3,4,5]:
    print(n)

for y in (1,2,3,4,5):
    print(y)



## While Loops: Use this to perform an action as lon as the condition is true

number = 10

while number > 0:
    print("Number is", number)
    number -=1      # decrementing number by 1 so the loop doesn't run infinitely


## ----- Handling user inputs with while loops: Letters game

# game = ""
# letter = ""

# while game != "complete":   # if you put game.lower() the loop can track "complete" in any case. for example "COMPLETE" OR "Complete" cuz it will convert input to lower case first before comparing
#     letter = input("Enter a letter > ")
#     game = letter
#     print("ECHO", game)



## ------  Complete little game :)

# l_game = ""
# l_letter = ""

# while "complete" not in l_game:   # as long the word is not in the input the game will go on
#     l_letter = input("Enter a letter > ")
#     l_game += l_letter    ## the game letters adds up. Instead of stand alone letters like above, I can create words now!
#     print("ECHO", l_game)



# Infinite Loops: Use this to perform an action as long as the condition is true. Unlike while loops, this will run until you stop it manually

# while True:
#     command = input("Enter a command >> ")
#     print("Show", command)
#     if command.lower() == "exit":         # termination checkpoint
#         print("program exited")
#         break


### Loop Exercise: print even numbers from 1 to 10 and display how many numbers were printed

# count  = 0
# for num in range(1,10):
#     if num % 2 == 0:
#         print(num)
#         count += 1
#     else:
#         continue
# print(f"We have {count} numbers")   # this is similar to but more efficient than print(f"We have" , count, "numbers")

