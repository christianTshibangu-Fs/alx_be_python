number = int(input("Enter the size of the pattern:"))
i = 0

while i < number and number > 0:
    for num in range(number):
        print("*", end="")
    print()
    i += 1