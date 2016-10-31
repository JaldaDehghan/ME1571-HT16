f = input("Enter fahrenheit: ")
f = int(f)
c =  f - 32 * 5.0/9.0

ce = input("Enter celcius: ")

fa = 9.0/5.0 * ce + 32

print(str(f) + " F in celcius: " + str(c))
print(str(ce) + " C in fahrenheit: " + str(fa))
