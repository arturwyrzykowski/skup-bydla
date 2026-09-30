# Bajka „Niewybuch” (odcinek 2) — projekt

Zatwierdzone przez usera 2026-09-30. Tylko lokalnie (bez publikacji).

## Cel
Drugi odcinek w stylu „Skup Bydła” (Blok Ekipa: grube kontury, płaskie kolory, dymki Comic Sans, wulgaryzmy zamierzone). ~50 s.

## Postacie
- **Saper 1** i **Saper 2** — obrazki `saper1.png`, `saper2.png` (karykatury od usera, tło wycięte). Ruch całą postacią: przesuwanie, bujanie (chód), podskok, odbicie lustrzane. Bez animacji kończyn.
- **Mirek** — kolega z busem, rysowany SVG w stylu odc. 1 (dres).
- **Złomiarz** — rysowany SVG (czapka, kufajka/kombinezon).

## Scenariusz
1. **Las, okop** (sosny, duży dół). Saperzy wchodzą z lewej; wykrywacz piszczy coraz szybciej.
   S2: „Ty, pika jak pojebane!” · S1: „Kopiemy. Tylko delikatnie, kurwa.”
2. **Kopanie**: szpadel rytmicznie, lecą grudy. Z dołu wyjeżdża wielka rdzawa bomba lotnicza, potem granat „cytrynka”.
   S1: „O ja pierdolę… ale sztuka!” · S2: „I granat gratis!” · S2 (telefon): „Mirek, podjeżdżaj busem, mamy towar.”
3. **Bus**: wjeżdża obdrapany biały bus, wysiada Mirek. M: „Ładować! Jedziemy na złom do Obrytego.” Ładunek do busa, odjazd w dymie.
4. **Droga**: bus podskakuje, mija tablicę „OBRYTE”, brzęk ładunku.
5. **Złomowisko „SKUP ZŁOMU OBRYTE”**: hałdy, waga. Z: „Dwieście kilo. Stówa i spadajcie.” · M: „Panie, to zabytek!” · Z: „To idź pan do muzeum.” Odjazd; złomiarz kopie bombę → BUM (błysk, trzęsienie), czapka leci w niebo. „KONIEC”.

## Technika
Jak odc. 1: jeden plik `bajka/niewybuch.html`, SVG 1600×900 + Web Animations API, sekwencja `async play()`. Scenerie jako osobne grupy `<g>` przełączane (las → droga → złomowisko). Dźwięki WebAudio: pisk wykrywacza, szpadel, silnik, brzęk, wybuch, telefon. Głosy: speechSynthesis (polski głos, różne pitch/rate dla postaci), fallback bla-bla. Nakładki start/koniec z przyciskiem (gest do dźwięku), obsługa klawiaturą (user bez myszy).

## Weryfikacja
Headless Chrome (puppeteer-core w scratchpad): zrzuty kluczowych momentów każdej sceny, brak błędów JS w konsoli, cały przebieg dochodzi do ekranu „KONIEC”.
