Ez a program egy egyszerű, grafikus naptár alkalmazás, amelyben eseményeket lehet hozzáadni és törölni a kiválasztott napokhoz.
A naptár hónapról hónapra lapozható, és minden esemény elmentődik egy JSON fájlba, így kilépés után sem vesznek el.

Fő funkciók:

Havi naptár megjelenítése (aktuális hónappal indul)
Hónap váltása: előző / következő hónap gombokkal

Események kezelése:

Esemény hozzáadása a kiválasztott naphoz
Esemény törlése listából
Adatok mentése fájlba (PF_events.json)
A program automatikusan létrehozza, ha nem létezik
Az események újra betöltődnek indításkor

Fájlok:

main.py – maga a program (ez a fájl tartalmazza a kódot)
PF_events.json – ebben tárolódnak az események (automatikusan jön létre)

Használat:

Python telepítése
Győződj meg róla, hogy a gépeden telepítve van Python 3 (pl. 3.10 vagy újabb).
Ellenőrzés:
python --version
Program futtatása
A fájl mappájában írd be:
python main.py

Használat a grafikus felületen:

A program indításakor megjelenik az aktuális hónap naptára.
Kattints egy napra, majd az „Esemény hozzáadása” gombbal adj meg egy új eseményt.
Az események a naphoz tartozó listában jelennek meg.
Kijelölt eseményt a „Esemény törlése” gombbal tudsz eltávolítani.
A „<< Előző hónap” és „Következő hónap >>” gombokkal lapozhatsz.

Mentés és betöltés:

A program automatikusan elmenti az eseményeket a PF_events.json fájlba.
Ha újraindítod a programot, az események újra betöltődnek.

Felépítés röviden:

A kód két fő részből áll:
PF_EventManager osztály
Az események kezeléséért és fájlba mentéséért felelős.
Feladatai:
események betöltése és mentése JSON fájlba
események hozzáadása és törlése adott naphoz

PF_CalendarApp osztály
A grafikus felületet (Tkinter) kezeli.
Megjeleníti a naptárat, kezeli a gombokat és az eseménylistát.

Kiegészítő információk:
A naptár a calendar és datetime modulokat használja a dátumkezeléshez.
A grafikus felület a tkinter könyvtárra épül.
A program magyar nyelvű felületet használ.

Készítette
Pemmer Ferenc István
Neptun kód: SL1N4I
Egyetemi beadandó céljából készült Python projekt.
