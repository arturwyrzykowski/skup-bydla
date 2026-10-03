# Odcinek 21 „Kulig” — projekt

Data: 2026-10-04. Scenariusz od usera, przebieg zatwierdzony („rób jak uważasz”).

## Cel

Pierwszy „profesjonalny” odcinek ZIOMKÓW: więcej zbliżeń, prawdziwy montaż (ujęcia zamiast scen), więcej szczegółów, styl Tarantino. Ta sama technika co dotąd (jeden plik HTML, SVG + Web Animations API), żeby działał na GitHub Pages i na telewizorze.

## Zasady stałe

- Bez dymków z tekstem; kwestie mówione głosami ElevenLabs (darmowe głosy, `dubbing.py`, obsada `POSTACIE`).
- Twarze tylko narysowane (SVG). Andrzej/Triwet/SYKET: głowy z `twarze_test.html`, usta ruszają się przy mówieniu (`.mC`/`.mO` + `flap()`).
- Incognito: sklep to „ALMA” (bez „ZAMBSKI”), postać Radka to zawsze „Triwet”.
- `<meta name="robots" content="noindex, nofollow, noarchive">`, intro `ziomkiIntro2("KULIG", 21, 3, 1)`, na końcu `ziomkiOutro()`.

## Postacie i stroje (zima)

| Postać | Strój / wygląd | Głos (darmowy) |
|---|---|---|
| Andrzej | czarna puchówka z parodią logo „adosis” (4 paski), beanie, rękawice | charlie |
| Triwet | granatowa kurtka, znaczek jak nike zakończony końcówką penisa, szalik | callum |
| SYKET | czerwona puchówka, uszanka na łysej głowie, plecak | laura |
| STIVEN | kufajka, zimowa czapka z daszkiem i nausznikami, gumiaki | bill |
| Aniela (NOWA) | różowa kurtka, czapka z pomponem, długi warkocz, rumieńce | jessica (`kobieta`) |
| Pablo | jajowata głowa (`pablo()` z postacie.py), rozpięta kurtka na koszuli | eric |
| Ratownik (NOWY) | czerwony kombinezon z odblaskami | daniel |

Mimika na zbliżeniach: przerażenie = okulary zjeżdżają na nos, widać wytrzeszczone oczy; Pablo po denaturacie = czerwone oczy.

## Przebieg (ok. 4–5 min)

Plansze rozdziałów na czarnym tle (styl Tarantino), pasy kinowe 2.39:1, ziarno filmu, winieta.

**ROZDZIAŁ I: ALMA** (zima, dzień). Chłopaki siedzą na skrzynkach pod sklepem ALMA, piwo Tatra, fajki, para z ust, padający śnieg. Zbliżenie: gil w nosie. Kwestie: „Może by zrobić kulig?” / „A sanki masz?” / „Nie.” / „To se pożyczymy.”

**ROZDZIAŁ II: SZKOŁA** (noc). Ciemna szkoła, snopy światła latarek w śniegu, komórka/szopa, wyciągają sanki; zbliżenie na tabliczkę „WŁASNOŚĆ SZKOŁY”; ucieczka z naręczem sanek.

**ROZDZIAŁ III: KULIG** (następny dzień). Ursus C-330 (STIVEN) ciągnie sznur sanek; chłopaki z fajkami w ustach, Aniela na sankach. Zbliżenie: Triwet wali setkę cytrynówki — „Andrzej.” / „Co?” / „Masz mordę jak kret, haha.” STIVEN jedzie wężykiem, startuje muzyka (własny energiczny podkład klubowy). Szybki montaż zbliżeń: komin i kłęby dymu; ogień strzela z tłumika; kokpit C-330 z obrotomierzem w czerwonym polu (rysunek wg zdjęć wnętrza z internetu); czerwone, rozpędzone tłoki; koła rwące lód i śnieg; przerażone oczy. Zakręt: Aniela przewraca się i spada, Triwet wjeżdża w nią sankami — stęk bólu + dziwaczny dźwięk uderzenia, zatrzymana klatka. Wstają. STIVEN: „Dobra, chyba kończymy.”

**ROZDZIAŁ IV: OGNISKO**. STIVEN rozpala ogień ropą z silnika (czarny dym), wyciąga kiełbasy z ciągnika; pieczenie. Andrzej, SYKET, Triwet robią flachę. Zza krzaka Pablo: „Macie lufę?” Triwet: „Mam schowaną w ciągniku.” Zbliżenie na butelkę denaturatu; dolewa ropy z silnika, miesza, za traktorem „dosikuje” (tylko plecy + dźwięk). „Smacznego.” Pablo pije → zbliżenie czerwonych oczu, efekt zawieszonego obrazu (zacinanie, glitch): „Eeee… błąd… błąd… system zawieszony.” Zesrał się i zeszczał (plama + dźwięk), pada na plecy jak trup.

**ROZDZIAŁ V: SOR**. Przywiązują Pablo do sanek, STIVEN jedzie ciągnikiem pod szpital z napisem „SOR”. Ratownik: kwestie „Nie znamy go.” / „Leżał na przystanku.” / „Trzeba go leczyć.” Zabierają go na noszach. Koniec → outro.

## Technika

- `bajka/kulig.html` budowany `bajka/build_ep21.py` (wzorem build_ep11+; wspólne kawałki z `postacie.py`, `ep15_parts.py`, build_ep13 itp.).
- **System ujęć:** każde ujęcie = osobna grupa SVG rysowana pod kadr (plan ogólny / średni / zbliżenie / detal), funkcje: `cut(shot)`, ruch kamery (najazd, odjazd, panorama, crash zoom), pasy kinowe, plansza rozdziału, ziarno + winieta (nakładka).
- **Detale:** śnieg (cząsteczki), para z ust, dym, ogień z tłumika, światło latarek (gradient + maska).
- **Dźwięk (WebAudio):** podkład klubowy do kuligu, silnik C-330, strzały z tłumika, stęk + dziwaczne uderzenie, glitch Pablo.
- **Głosy:** `dubbing.py` (CAST dla `kulig`), efekt zacinania dla kwestii Pablo „system zawieszony”. Budżet ~500–600 znaków (zostało ok. 1000 w miesiącu). Potem `fix_audio.py`.
- Podglądy rozdziałów bez intra: `#alma`, `#szkola`, `#kulig`, `#ognisko`, `#sor`.
- Publikacja: dopisać do `hejczbiolgo.html` (EPS) + miniatura `miniatury/kulig.jpg`.

## Testy

- Po każdym rozdziale: zrzuty ujęć (headless Chrome, `--mute-audio`, wirtualny czas z `dub_capture.FAST`) i obejrzenie ich.
- Brak błędów JS przy ładowaniu i przy przebiegu całego odcinka.
- `dub_capture.py` wyłapuje wszystkie kwestie; każda ma nagranie.
