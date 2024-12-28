# MC-Körkortsbot 🏍️

MC-Körkortsbot är en Python-baserad bot som automatiskt söker efter lediga tider för körprov (kategori A) via Trafikverkets bokningssystem. Boten är idealisk för att snabbt hitta tillgängliga tider och skickar notifieringar till en Discord-kanal när en tid hittas.

---

## 🛠 Funktioner
- **Automatisk inloggning**: Loggar in på Trafikverkets bokningssystem med ditt personnummer (kräver Bank-ID).
- **Sökning av körprovstider**: Sökning sker på förvalda orter som du kan konfigurera.
- **Notifieringar via Discord**: Skickar meddelande till en angiven Discord-kanal om lediga tider hittas.
- **Fjärrstyrning via Discord**: Möjlighet att stoppa boten genom att skriva "stop" i Discord-kanalen.

---

## 🚀 Kom igång

### 📋 Krav
- Python 3.8 eller högre.
- [Selenium](https://www.selenium.dev/) och ChromeDriver.
- Ett giltigt Discord-token.
- Ditt personnummer (säkerställ att detta hanteras säkert).

### 📦 Installation
1. **Klona detta repository**:
   ```bash
   git clone https://github.com/ditt-användarnamn/mc-korkortsbot.git
   cd mc-korkortsbot
Installera beroenden:

bash
Copy code
pip install selenium requests
Ställ in miljövariabler: Skapa en .env-fil eller ställ in följande variabler:

makefile
Copy code
DISCORD_TOKEN=din_discord_token
PERSON_NUMBER=ååååmmddxxxx
CHROME_DRIVER_PATH=C:/Program Files (x86)/chromedriver.exe
Anpassa orter: I koden finns en lista över orter (listofplaces). Uppdatera denna lista med de orter där du vill söka efter körprov.

🔧 Användning
Starta boten:

bash
Copy code
python bot.py
Följ instruktionerna i terminalen:

Ange ditt personnummer.
Logga in med Bank-ID när du blir ombedd.
Notifieringar: Boten söker automatiskt efter körprovstider och skickar notifieringar till din Discord-kanal.

Stoppa boten: Skriv stop i den anslutna Discord-kanalen för att avsluta boten.

⚠️ Viktigt
Boten är endast till för personligt bruk.
Trafikverkets bokningssystem ska användas enligt deras regler och villkor.
Säkerställ att du hanterar din personliga information, som personnummer och Discord-token, på ett säkert sätt.
🖼️ Exempel på notifieringar
Så här kan ett meddelande från boten se ut i Discord:

yaml
Copy code
Finns tid: 2022-06-21 i Västerås
📜 Licens
Den här boten är öppen källkod och tillgänglig under MIT-licensen.

💡 Feedback och bidrag
Om du har förbättringsförslag eller hittar buggar, tveka inte att skapa en issue eller skicka in en pull request!

📞 Kontakt
Om du har frågor kan du nå mig på: din.email@exempel.com

bash
Copy code

Den här README-filen är strukturerad och anpassad för GitHub. Den innehåller rubriker, kodblock och en tydlig layout för att göra det enkelt för andra att använda och förstå projektet. Låt mig veta om du behöver ytterligare hjälp! 😊
