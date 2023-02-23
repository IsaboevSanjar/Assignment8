number = int(input("Enter the input Range : "))
print(f"Prime numbers: <= {number} are:", end=" ")
for i in range(2, number + 1):
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        print(i, end=" ")
