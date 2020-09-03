num_int = 0
max_int = 0
high_int = 0
while num_int >= 0:
    num_int = int(input("Input a number: "))  # Do not change this line
    high_int = num_int
    if max_int < num_int:
        max_int = num_int
        continue
    # Fill in the missing code
print("The maximum is", max_int)  # Do not change this line
