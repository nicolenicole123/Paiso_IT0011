for i in range(1, 6):
    for j in range(1, 6 - i):  # Print spaces
        print(" ", end="")
    for k in range(1, i + 1):  # Print numbers
        print(k, end="")
    print()

print(" ")
i = 1
while i <= 7:
    j = 1
    while j <= (i - 1) // 2:
        print("", end="")
        j += 1
    num = i
    while num > 0:
        print(i, end="")
        num -= 1
    print()
    i += 2



