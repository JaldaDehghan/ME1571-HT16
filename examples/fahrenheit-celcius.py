f = input("Enter fahrenheit: ")
c =  round(f - 32 * 5.0/9.0, 1)
print(str(f) + " degrees fahrenheit is Celcius: " + str(c))

print("-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-")

ce = input("Enter celcius: ")
fa = round(9.0/5.0 * ce + 32, 1)
print(str(ce) + " degrees celcius is Fahrenheit: " + str(fa))
