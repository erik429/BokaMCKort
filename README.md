MC-Körkortsbot
Den här boten är skapad för att automatiskt leta efter tillgängliga tider för körprov för MC (kategori A) via Trafikverkets bokningssystem. Boten loggar in på bokningssidan, söker igenom olika platser och skickar notifikationer via en Discord-kanal om den hittar en tillgänglig tid.

Funktioner
Automatisk inloggning: Boten loggar in på Trafikverkets bokningssystem med ditt personnummer (Bank-ID krävs).
Sökning av körprovstider: Boten söker igenom förvalda orter för att hitta lediga tider för körprov.
Notifieringar via Discord: Om en ledig tid hittas skickar boten ett meddelande till en fördefinierad Discord-kanal.
Fjärrstyrning via Discord: Du kan stoppa boten genom att skriva ordet "stop" i den kopplade Discord-kanalen.
Krav
Python installerat (version 3.8 eller högre).
Selenium och ChromeDriver installerat.
Ett giltigt Discord-token för att skicka och läsa meddelanden.
Ditt personnummer för att logga in på Trafikverket (säkerställ att detta hanteras säkert).
Konfiguration
Installera nödvändiga bibliotek:

bash
Copy code
pip install selenium requests
Miljövariabler: Skapa en .env-fil eller ställ in följande variabler:

DISCORD_TOKEN: Ditt Discord-token.
PERSON_NUMBER: Ditt personnummer (format: ååååmmddxxxx).
CHROME_DRIVER_PATH: Sökvägen till din ChromeDriver.
Förbered lista över orter: Ändra listofplaces i koden för att inkludera orterna du vill söka på.

Så här kör du boten
Starta skriptet:
bash
Copy code
python bot.py
Följ instruktionerna i terminalen:
Ange personnummer.
Logga in med Bank-ID när du blir uppmanad.
Boten börjar söka efter tider och skickar notifikationer till Discord-kanalen.
Viktigt
Den här boten är endast till för personligt bruk.
Trafikverkets bokningssystem ska användas enligt deras regler och villkor.
Säkerställ att du hanterar din personliga information (som personnummer och Discord-token) på ett säkert sätt.
