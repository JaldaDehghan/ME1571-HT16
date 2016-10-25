# Övningar vecka 1 -2

## age.py
 _importera datetime modulen (kolla i dokumentationen)_
 
- använd datetime.datetime() för att skapa en variabel som representerar datumet du föddes 
- använd datetime.datetime.now() för att skapa en variabel som representerar nu
- subtrahera variablerna, till en ny variabel, som kommer att bli ett datetime.timedelta() objekt. Printa den variabeln.


**Ditt script ska kunna skriva ut svar på följande frågor:**

1. hur många dagar har du levt? Hur många timmar? 
2. Vilket datum är det om 1000 dagar? 



## age1.py

_Använd_ `__name__ == “__main__”` _i ditt script_


- när scriptet körs från command line/prompten med 1 argument, ska age1.py kunna printa datumet i dagar från nu. 
- Gör en funktion.

Exempel på körning:

Mac/Linux: `$ ./age1.py 1000`

Win: `C:\python age1.py 1000`

`date in 1000 days 2016-07-15 13:15:58.390970`



- om scriptet körs med 3 argument, printa tiden i dagar från datumet
- Gör en ny funktion.

Exempel på körning:
`$ ./age1.py 1980 1 8`
