# Kod för L18 – Matematik i C med math.h
Exempelprogram och lösningar till lektionsuppgifterna i [bilaga B](../appendix/b_exercises.md).

## Utvecklingsmiljö
Under lektionen används **OnlineGDB**, en `gcc`-kompilator som körs direkt i webbläsaren:

<https://www.onlinegdb.com/online_c_compiler>

Ingen installation krävs, och inget konto behövs.

**1.** Kontrollera att språket är inställt på **C** i listan uppe till höger.\
**2.** Skriv koden i editorn.\
**3.** Tryck på **Run**. Utskriften hamnar i rutan under editorn.

**OBS!** Koden sparas inte automatiskt. Kopiera den till en egen fil innan ni stänger fliken.

### Matematikbiblioteket
Funktionerna i `math.h` och `complex.h` ligger i ett separat matematikbibliotek, `libm`. Vid felmeddelandet `undefined reference to 'sqrt'` länkas det inte in – lägg då till `-lm` under **Extra Compiler Flags** i inställningarna (kugghjulet).

### Sampelvärden till diagram
Program som skriver ut sampelvärden som CSV körs i OnlineGDB på vanligt sätt. Markera utskriften i utdatarutan, kopiera den och klistra in den i ett kalkylprogram för att rita upp signalen.

---

## Kompilering på egen dator (frivilligt)
Ingenting under lektionen kräver detta – OnlineGDB räcker hela vägen. **WSL** med `gcc` och `make` används däremot i senare kurser, så den som vill kan sätta upp miljön redan nu.

### 1. Installera WSL
WSL *(Windows Subsystem for Linux)* gör det möjligt att köra en Linux-distribution i en terminalmiljö direkt i Windows, utan att använda en virtuell maskin. Här används distributionen **Ubuntu**.

Installationen kräver **administratörsrättigheter** samt en omstart.

**a)** Öppna **Windows PowerShell** som administratör.\
**b)** Kör följande kommandon:

```powershell
wsl --install
wsl --set-default-version 2
```

Alternativt kan Ubuntu installeras direkt med:

```powershell
wsl --install -d Ubuntu
```

**OBS!** Om systemet begär en omstart, starta om datorn innan du fortsätter.

**c)** Verifiera installationen med kommandot nedan, och kontrollera att **Default Version: 2** visas:

```powershell
wsl --status
```

**Om installationen misslyckas:**
* WSL kräver Windows 11, eller Windows 10 version 2004 (build 19041) och senare.
* Virtualisering måste vara aktiverat i datorns UEFI/BIOS. Är det avstängt måste det slås på där.
* Saknas administratörsrättigheter går WSL inte att installera – använd OnlineGDB i stället.

### 2. Installera Ubuntu
Om Ubuntu inte installerades via PowerShell:

**a)** Öppna **Microsoft Store**.\
**b)** Sök efter `Ubuntu`.\
**c)** Välj den senaste LTS-versionen.\
**d)** Klicka på **Installera**.

### 3. Starta Ubuntu
Skriv `Ubuntu` i Windows sökfält och starta distributionen. Vid första uppstarten:
* Välj ett kort och tydligt användarnamn, exempelvis ditt förnamn.
* Välj ett lösenord och spara det på ett säkert ställe.

**OBS!** Lösenordet syns inte medan det skrivs in – det är normalt. Lösenordet används endast i Linux-miljön.

### 4. Installera utvecklingsverktyg
När Ubuntu har startat, uppdatera systemet och installera nödvändiga verktyg:

```bash
sudo apt -y update
sudo apt -y upgrade
sudo apt -y install build-essential
```

Detta installerar bland annat `gcc`, `make` samt olika utvecklingsbibliotek. Verifiera installationen:

```bash
gcc --version
make --version
```

### 5. Kompilera för hand
Flaggan `-lm` länkar matematikbiblioteket och måste placeras **efter** källkodsfilerna:

```bash
gcc main.c -o main -lm
./main
```

Använd `gcc`:s standardläge (eller `-std=gnu11`) om ni vill använda konstanten `M_PI`. I strikt standardläge (`-std=c11`) är den inte definierad, och då får ni definiera $\pi$ själva.

Utskriften kan sparas direkt till en fil genom omdirigering, vilket är smidigare än att kopiera från utdatarutan:

```bash
./samples > samples.csv
```

Filen kan sedan öppnas i ett kalkylprogram eller läsas in i en simulator som ritar upp signalen.

### 6. Kompilera med make
För varje program, skapa en ny katalog och en fil som heter `Makefile`:

```bash
mkdir example-dir
cd example-dir
touch Makefile
```

I denna makefile lägger du till följande innehåll:

```makefile
# Build and run the application as default.
default: build run

# Build the application.
build:
	@gcc main.c -o main -Wall -Werror -std=gnu11 -lm

# Run the application.
run:
	@./main

# Clean the application.
clean:
	@rm -f main
```

**Notera:**
* Indenteringen under målen `build`, `run` och `clean` måste bestå av **tabbar**, inte mellanslag.
* Denna makefile bygger en körbar fil med namnet `main`.
* Angående kompilatorflaggorna:
    * `-Wall` aktiverar de flesta kompilatorvarningar.
    * `-Werror` omvandlar varningar till fel, vilket hjälper till att förhindra subtila buggar.
    * `-std=gnu11` anger att C-versionen är C11 med GNU-tillägg, vilket gör `M_PI` tillgänglig.
    * `-lm` länkar matematikbiblioteket och placeras **sist**, efter källkodsfilerna.
* För att se kompilationskommandona som körs av make, ta bort prefixet `@`.

#### Makefile med parametrar
Det är också möjligt att använda parametrar för att göra makefilen lättare att underhålla, särskilt när antalet källfiler ökar:

```makefile
# Target application.
TARGET := main

# C compiler.
CC_COMPILER := gcc

# C compiler flags.
CC_FLAGS := -Wall -Werror -std=gnu11

# Linker flags. The math library must be linked after the source files.
LD_FLAGS := -lm

# Source files.
SOURCE_FILES := main.c

# Build and run the application as default.
default: build run

# Build the application.
build:
	@$(CC_COMPILER) $(SOURCE_FILES) -o $(TARGET) $(CC_FLAGS) $(LD_FLAGS)

# Run the application.
run:
	@./$(TARGET)

# Clean the application.
clean:
	@rm -f $(TARGET)
```

Fler källkodsfiler läggs till en per rad med radfortsättning (`\`):

```makefile
SOURCE_FILES := derivative.c \
                integral.c \
                main.c \
```

### 7. Bygga och köra
```bash
make        # Bygg och kör programmet.
make build  # Bygg programmet utan att köra det.
make run    # Kör programmet utan att bygga om det.
make clean  # Ta bort kompilerade filer.
```

### 8. Filer och editor
* Windows-filerna nås från Ubuntu under `/mnt/c/`, exempelvis `/mnt/c/Users/<användarnamn>/Desktop`.
* Arbetet går snabbare om filerna i stället ligger i Linux-hemkatalogen, `~`.
* **VS Code** med tillägget **WSL** öppnar filerna direkt i Ubuntu-miljön. Skriv `code .` i terminalen för att öppna aktuell katalog.

---

## Kodformattering
C-koden i denna katalog formatteras med `clang-format` via [ci/format.sh](../../../ci/format.sh):

```bash
ci/format.sh          # Formatera alla filer.
ci/format.sh --check  # Kontrollera formattering utan att ändra filer.
```

---

## Licens
Koden i denna katalog är licensierad under [MIT](./LICENSE), separat från kursmaterialets [CC BY 4.0](../../../LICENSE).

---
