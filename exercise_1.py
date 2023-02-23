numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))


def common(a, b):
    if b == 0:
        return "No Solution"
    elif a == 0:
        return 0
    while b != 0:
        (a, b) = (b, a % b)
    return f"{int(numerator / a)}/{int(denominator / a)}"


print(f"{int(numerator)}/{int(denominator)}=", common(numerator, denominator))