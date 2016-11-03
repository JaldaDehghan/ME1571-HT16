choice = raw_input("Area for (r)ectangle or (t)riangle? ")

if choice == "r":
    s1 = input("Enter rectangle length of side 1: ")
    s2 = input("Enter rectangle length of side 2: ")

    area = s1 * s2

    print("Area of rectangle is " + str(area))
elif choice == "t":
    b = input("Enter triangle base length: ")
    h = input("Enter triangle height: ")

    area = (b * h) / 2

    print("Triangle area is " + str(area))
else:
    print("Not valid format.\nExiting.")
