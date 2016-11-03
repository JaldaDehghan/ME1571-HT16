eur = 0.100935773 # 1 SEK = 0.100935773 [161101]

print("THIS APP WILL CALC INPUT IN SEK TO EUROS")
sek = input("Enter amount of SEK: ")

sum = round(sek * eur, 2)

print(str(sek) + "SEK is "+ str(sum) + "EUR.")
