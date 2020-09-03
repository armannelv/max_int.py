n = int(input("Enter the length of the sequence: ")) # Do not change this line

round_1 = 1
round_2 = 2
round_3 = 3
final = 0
print(round_1)
print(round_2)
for i in range(1, n - 2):
    final = round_1 + round_2 + round_3
    round_1 = round_2
    round_2 = round_3
    round_3 = final
    print(final) 