def area(height, base):
    sum = (height * base) / 2
    return sum


height = input("Enter height: ")
base = input("Enter base: ")

height = int(height)
base = int(base)

print(area(height, base))
