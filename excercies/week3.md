# Övningar vecka 3

Övningarnas syfte är att du ska bekanta dig med klassbegreppet och objekt, dvs grundläggande OOP i python.
Detta i form av att skapa klasser med funktioner, variabler etc i, samt att skapa objekt av och mellan klasserna.


## student
### Gör en klass som representerar studenter på din utbildning.
+ Lägg till attribut i klassen som representerar namn, ålder, akronym, email och github-nick.
+ Lägg till en metod som gör att github-nick går att ändra (man ska alltså kunna uppdatera en students gihub-nick).
+ Lägg till en metod som returnerar en URL för github-nicket. Om github-nick är h3llo, så ska metoden returnera följande sträng;
  http://github.com/h3llo

Få med följande:
- konstruktor
- nödvändiga funktioner
- ett script/fil bredvid som skapar objekt av din klass och som använder metoderna.

## program
Bygg vidare på ovanstående lösning och implementera;
+ ytterligare en klass som representerar ett program med studenter i (dvs studentobjekt i en klass).
+ gör metoder som erbjuder att studenter kan läggas till i, eller tas bort från programmet 
  (dvs nya studenter ska kunna påbörja utbildnignen och studenter ska kunna avlsuta utbildningen)
+ lägg till metoder som ger utskriftvänliga versioner av student-, och program-objekt.
+ via ett program-objekt ska man kunna söka efter en student, skriva ut en student och göra det som studentklassen erbjuder.
+ gör ett script bredvid som skapar ett antal program med flera studenter i respektive program.

Om du vill - gör ytterligare en klass som du kallar University. University ska representera en skola med flera program i.


## farmer john
Nu en övning med flera klasser med metoder, variabler etc i, samt att skapa objekt av och mellan klasserna.


Gör ett program som simulerar en bondgård. Skapa klasser som gäller för de djur som finns på bondgården (minst 3st djur). 
Djuren ska ha egenskaper och attribut (minst tre av varje). Attributen kan vara till exempel namn, ålder, vikt, storlek etc. 
Egenskaperna ska vara funktioner som till exempel kan vara springa, sova, äta, åldras etc etc.
Själva bondgården ska vara en klass som innehåller alla djuren.
En användare ska kunna skapa bondgårdar och kunna köpa nya djur och sälja befintliga djur som då tillhör en viss bondgård.

Du kan självklart översätta bondgården till något annat kontext.

Försök att få med åtminstone:
+ använd klasser med funktioner, variabler (medlemmar/attribut) och skapa objekt av klasserna.
+ skapa klasserna i egna moduler/filer.
+ skapa en fil/ett script i vilken programmet startas.
+ programmet ska kunna exekveras utan fel, men du behöver inte ta hänsyn till om en användare matar in ‘fel’ data.
+ programmet ska kunna skriva ut alla användarens bondgårdar med alla djur och djurens attribut.



## Soccer
Gör ett pythonprogram som simulerar flera fotbollslag. Skapa klasser för spelare, lag, tränare och en fil som hanterar 
allt (dvs skapar objekt av klasserna, presenterar menyer etc).


En användare ska kunna skapa flera lag. En användaren ska kunna skapa tränare och spelare till ett specifikt lag. 
Användaren ska kunna skriva ut information om lagen och då se vilka spelare och tränare som tillhör respektive lag.


Lag, spelare och tränare ska vara egna klasser i egna filer.
I ett lag ska kunna finnas flera spelare och flera tränare.
Alla klasserna ska ha attribut och egenskaper.

För att nå upp till följande:
+ använd klasser med funktioner, variabler (medlemmar/attribut) och skapa objekt av klasserna.
+ skapa klasserna i egna moduler/filer.
+ skapa en fil/ett script i vilken programmet startas.
+ programmet ska kunna exekveras utan fel, men du behöver inte ta hänsyn till om en användare matar in ‘fel’ data.
+ programmet ska kunna skriva ut alla användarens lag med alla spelare och spelarnas attribut.
