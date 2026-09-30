# Niewybuch (odcinek 2) Implementation Plan

**Goal:** Plik `bajka/niewybuch.html` — animowana bajka wg specu `docs/superpowers/specs/2026-09-30-niewybuch-design.md`.

**Architecture:** Jeden plik jak odc. 1: SVG 1600×900, trzy scenerie (`#scForest`, `#scRoad`, `#scYard`) przełączane z wygaszeniem (`#fade`), wspólna warstwa aktorów (saperzy jako `<image>`, Mirek i złomiarz jako SVG, bus). Sekwencja `async play()`, Web Animations API, dźwięk WebAudio, głosy speechSynthesis.

**Tech Stack:** HTML/SVG/JS bez bibliotek. Weryfikacja: puppeteer-core + Chrome w scratchpad.

- [ ] 1. Scenerie: las z okopem (clipPath dla bomby w dole), droga z tablicą OBRYTE, złomowisko z wagą i szyldem. Zrzut statyczny każdej.
- [ ] 2. Rekwizyty i postacie: bomba i granat (`<defs>` + `<use>`), szpadel, bus (koła, kierowca w oknie), Mirek, złomiarz (czapka `zCap`, noga `zLegR`), saperzy z `saper1.png`/`saper2.png`.
- [ ] 3. Silnik: dźwięki (pisk wykrywacza, szpadel, silnik, brzęk, telefon, wybuch), dymki + mowa (reuse z odc. 1), ruch aktorów, zmiana scen.
- [ ] 4. Sekwencja scen 1–5 wg specu.
- [ ] 5. Weryfikacja: puppeteer — brak błędów konsoli, zrzuty kluczowych momentów, dojście do „KONIEC”. Commit lokalny (bez push).
