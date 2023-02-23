number = abs(int(input("Enter a positive integer here: ")))


def maximum_value(num):
    total = 1
    max_value = 0
    for i in range(1, num):
        for j in range(i + 1):
            total *= i
        if total > num:
            max_value = i
            break
        total = 1
    return max_value


print(f"Input y: {number}")
print(f"Maximum x = {maximum_value(number)}")
