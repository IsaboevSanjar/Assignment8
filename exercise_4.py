def print_border(num, space):
    index = 0
    for i in range(num * space):  # replace with multiplication   num * space 15 was here
        if i == index:
            print("+", end=" ")
            index += space
        print("-", end=" ")
        if i == num * space - 1:
            print("+")


def print_vertical(num, space):  # the same concept applies here..
    index = 0
    for i in range(num * space):
        if i == index:
            print("|", end=" ")
            index += space
        print(" ", end=" ")
        if i == num * space - 1:
            print("|")


N = int(input("Input the number of elements: "))
n = int(input("Enter a number: "))

print_border(N, n)
for i in range(n):
    print_vertical(N, n)
print_border(N, n)
