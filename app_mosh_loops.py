
# For loops

for num in range(4):
    print("Number:" , num)

for num in range(4 , 10):  ## this says = from this number to this (4,5)
    print("Number is", num, num + 2)

for num in range(1, 14, 3):  ## this handles additions automatically, the last number says skip these spots to the next number within the range
    print("Number with steps is", num)


## For... Else loop

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


## Iterables: list, tuple, dictionary, set, range, string