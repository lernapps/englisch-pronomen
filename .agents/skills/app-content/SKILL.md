---
name: app-content
description: Use for any content work in this app - researching, writing, extending, correcting or reviewing its competencies, chapters, pages, rounds, questions, exercises, figures, terms or sources. This app's own content decisions; they take precedence over the generic lernapps content skills. Load it before you change any content.
---

# Content guide of this app

Pronomen: I, me, my (Titel in `src/app.yaml`; er wird mit dem Inkrement für Kapitel 2 wieder zu „Pronomen: I, me, my, mine, myself“ erweitert). Explainer (Strang-App `englisch/grammatik`, Stufe 5-6, Sprache Deutsch). Auftrag: Issue lernapps/apps#471. Gebaut ist Kapitel 1 „Wer? Wen? Zu wem?“; Kapitel 2 (Stufe 7-8) kommt später.

## Curriculum

Englisch als erste Fremdsprache, Klasse 5-6. Kein Lehrplan: Reihenfolge und Bausteine kommen aus der Lernlandkarte `https://lernapps.net/apps/map/englisch.json` (Fokus `competency`). Vorwissen: Hello, Millbrook! (noun, verb, adjective, sentence, tense). Nicht hier: Demonstrativbegleiter, some/any (#475), Relativpronomen (#481), Formen von to be (#472); mine/yours, myself, each other kommen in Kapitel 2.

## Competencies

Kapitel `pronomen-1` („Wer? Wen? Zu wem?“), vier Seiten:

1. `personalpronomen`: Ich kann die Personalpronomen als Subjekt (I, he, they) und als Objekt (me, him, them) richtig verwenden. → `pronomen-1/wer-tut-es` (Subjekt), `pronomen-1/wen-trifft-es` (Objekt)
2. `possessivbegleiter`: Ich kann mit my, your, his, her, its, our und their sagen, wem etwas gehört. → `pronomen-1/my-your` (my, your, our, their), `pronomen-1/his-her` (his, her, its)

Beide Kompetenzen sind Lücken der Karte, `personalpronomen` hat keine Voraussetzung, `possessivbegleiter` verlangt `personalpronomen` (steht früher). Kein `ahead`, keine Wiederholungsseite. Übungs-IDs: Präfix = Seite (`wer-…`, `wen-…`, `my-…`, `his-…`). Je Seite: `<p>-start` (single-choice im Einstieg), `-zuordnen` (matching, Seiten 1 bis 3), `-waehlen` (language-task choice), `-schreiben` (write mit `mistakes`), `-falsch`/`-it` (true-false), `-hoeren` (Diktat), `-tabelle` (Tabelle ausfüllen), `-nachsprechen` (speaking-task); Seite 2 zusätzlich `wen-ordnen` (ordering), Seite 3 `my-luecke` (gap), Seite 4 `his-richtig`, `his-gemischt` (choice mit mehreren Lücken) und `his-frei` (open-task). Selbsteinschätzung in `src/pronomen-1/chapter.yaml`: je Seite `-waehlen` und `-schreiben`, zusammen acht Übungen.

## Content structure

- Pfad: `src/pronomen-1/chapter.yaml`, Seiten `src/pronomen-1/<seite>.yaml`.
- Jede Seite hat dieselben Abschnitts-IDs: `einstieg` (Szene, erste leichte Aufgabe, „Das kannst du danach“), `neu` (Tabelle wächst, Kasten „Merke“), `uebung` (mindestens vier Übungen, leicht → schwer), `anwenden` (`speaking-task` oder `open-task`), `weiter` (nächster Schritt der Geschichte; Seite 4 mit Rückblick). Titel sagen, was der Abschnitt tut.
- Länge: höchstens 350 Wörter Text, höchstens 4 Textblöcke hintereinander, Bild oder Übung unter den ersten vier Blöcken.
- Geschichte: Sophie (11, blond, Zöpfe, grüne Jacke, aus Deutschland, wohnt bei den Parkers), Ellie Parker (11, roter Pferdeschwanz, rote Jacke), Peter Parker (9, kurze braune Haare, gelbe Jacke, Ellies Bruder), Amir (11, schwarze Locken, Brille, blaue Jacke), Mr Hill (Englischlehrer, graue Haare, braune Jacke), Mrs Parker (Ellies Mutter, Sophies Gastmutter). Millbrook School, erfundene Schule in einer englischen Kleinstadt, Schultag beginnt 8:45. Geburtstage: Peter 5. Mai, Ellie 10. Juli, Amir 12. Oktober, Sophie 14. Oktober. Je Seite eine Szene mit kurzen Sätzen und Dingen aus dem Alltag.
- Alle Beispielsätze nutzen `can` mit see, help, call, swim, run, sing, jump, read, damit das Verb sich nicht ändert (kein -s). Nomen: bag, jacket, ball, book(s), brother, sister, cat; sie stehen vor den Übungen auf der Seite.
- Das wachsende Bild: Tabelle „Klassenzimmer-Poster · Pronomen“ (Seite 1: Person · Wer tut es?; Seite 2 + Wen trifft es?; Seite 3 + Zu wem gehört es? für I, you, we, they; Seite 4 alle Zeilen; Zeilenkopf = deutsches Wort ich, du / ihr, er, sie (ein Mädchen), es, wir, sie (mehrere), `rowHeaders: true`). Seite 4 hat zusätzlich die Figur `images/his-her-person.svg` (Pfeile von der Person zu ihrem Bruder oder ihrer Schwester: her brother, his sister). Die Tabelle steht nicht direkt über der Übung, die sie beantwortet.

## Terminology

- Nie „Besitzer“ oder „Ding“, wenn es um Menschen geht (her brother, his sister): „die Person, zu der es gehört“; was dazugehört: „Person oder Sache“. Spalte 3 heißt „Zu wem gehört es?“ (Rückmeldung des Erstellers; im Issue stand „Wessen Ding?“). Bild `src/images/his-her-person.svg`.

- Anrede „du“; „Ausdruck“ (fester Ausdruck), nie „Wendung“. Britisches Englisch, kein deutsches Wort in einem englischen Satz.
- Fachbegriffe noun, verb, adjective, sentence, tense gelten. „Subjekt“ (wer tut es) und „Objekt“ (wen trifft es) werden auf den Seiten 1 und 2 erklärt, wo sie gebraucht werden; „Possessivbegleiter“ als „Wort, das sagt, wem etwas gehört“.
- Aussprache nur als Lesehilfe in deutscher Annäherung, betonte Silbe in Großbuchstaben, keine Lautschrift (gehört in #482).
- Englische Wörter immer mit deutscher Bedeutung beim ersten Auftreten; Übungen fragen nur Wörter ab, die vorher auf der Seite stehen.

## Exercise patterns

Von leicht zu schwer: wählen (`matching`, `single-choice`) → Lücken und Formen wählen (`language-task` mode `choice`/`gap`) → Tabelle ableiten (`language-task` mode `table`) → schreiben (`write`, Deutsch → Englisch, `mistakes`) → korrigieren → hören (Diktat) und nachsprechen.

- Person ↔ Pronomen zuordnen: `matching` (Seite 1).
- Subjekt oder Objekt wählen: `language-task` mode `choice` mit `distractors`.
- Tabelle ableiten (I – me – my): `language-task` mode `table`.
- Die Person, zu der es gehört, bestimmt his/her: `matching` und `language-task` mode `choice`, Seite 4.
- Satz bauen: `ordering`.
- Hören/Nachsprechen: `language-task` mit `audio`, `speaking-task`; Audio: Stimme `bf_emma`, nur ganze Sätze, Dateien `src/audio/<satz-in-kleinbuchstaben>.mp3`.
- Je Fehlertyp eine Rückmeldung in `mistakes`: I/me, he/him, his/her nach der Person oder Sache, die dazugehört, statt nach der Person, zu der sie gehört, its/it's.
- Keine Datendateien, keine Vue-Komponenten.

## Figures

- Je Seite eine Szene `src/images/szene-wer-tut-es.svg`, `szene-wen-trifft-es.svg`, `szene-my-your.svg`, `szene-his-her.svg` (erzeugt aus den Figuren-Definitionen von Hello, Millbrook!; die Figuren stehen als `<g id=…>` in `<defs>`), eigene Zeichnung (Quelle „eigene Zeichnung“, Lizenz CC-BY-4.0), Figuren aus `millbrook-klassenzimmer.svg` von hello-millbrook kopiert (`<g id="…">`). `alt` sagt, was die Szene zeigt, nie die Lösung; die Caption sagt, worauf man achtet. Beschriftungen innerhalb des `viewBox`, funktioniert bei 360 px.

## Sources

Karte `https://lernapps.net/apps/map/englisch.json`. Fakten (nicht Sätze) aus Wikipedia „Personal pronouns in English“ und „Possessive determiner“ (CC BY-SA): die Formen I/me/my, you, he/him/his, she/her, it/its, we/us/our, they/them/their; my, your, his, her, its, our, their stehen vor dem Nomen, mine/yours gehören nicht dazu. Klexikon und de.wikipedia nicht geöffnet (ungeprüft). Audio: KI-Stimme britisch weiblich, mit Skill `lernapps-audio`, als KI-generiert markiert.

## Adding a chapter or round

1. Baustein auf der Karte wählen (Kapitel 2: `possessivpronomen`, `reflexivpronomen`, `each-other`; Voraussetzungen müssen früher stehen).
2. Kapitel `src/pronomen-2/chapter.yaml` und Seiten mit den Abschnitten `einstieg`, `neu`, `uebung`, `anwenden`, `weiter` anlegen, in `src/app.yaml` unter `chapters` eintragen, Competency-ID eintragen.
3. Die Tabelle „Klassenzimmer-Poster · Pronomen“ um zwei Spalten erweitern (mine/yours, myself; each other als eigener Kasten).
4. Übungen aus den Mustern oben, je mit `mistakes` und `hint`; 1 bis 3 Übungen in `selfAssessment` (Skill `lernapps-explainer-self-assessment`).
5. Hörtexte mit `.agents/skills/app-content/scripts/regen_audio.py` erzeugen und anhören lassen.
6. `npx --no -- lernapps check`, committen.

## Rules learned from mistakes

- Hörsätze (Diktat und Nachsprechen) stehen nicht (fast) wörtlich im Text, im Kasten Merke, in Bildern oder in einer anderen Übung derselben Seite; die Lösung einer Übung steht nicht wörtlich im Text, Bild oder Poster direkt darüber. Distraktoren sind echte Lernerfehler, je mit eigener Meldung in `mistakes`. Je Seite höchstens eine kurze Wörtertabelle (das Poster).
- Übernommen aus Hello, Millbrook!: Jede Übung fragt nur Wörter, die vorher auf der Seite stehen; eine Tabelle, die eine Übung beantwortet, steht nicht direkt darüber; Auswahlaufgaben zur Großschreibung zeigen alle Optionen gleich; gleichwertige Antworten mit `(a|b)`; Tabellenzellen und Texte mit `: ` oder Komma in Anführungszeichen.
- Audio: Die Stimme hängt an kurzen Sätzen ein Ausklingen an; alle Dateien entstehen mit `regen_audio.py` (im Ordner der App, mit dem Python der Audio-Umgebung `~/.cache/lernapps/audio/venv/bin/python`). Namen am Satzende zweisilbig (Sophie, Peter, Ellie). Hörsätze bleiben natürlich: Es wird kein Name nur wegen des Klangs angehängt. Das Ausklingen schneidet `regen_audio.py` ab (alle Sätze samt Dateinamen: `.agents/skills/app-content/audio-texte.json`; Aufruf `python regen_audio.py audio-texte.json "<Satz>"`). Zusätzlich schneidet `regen_audio.py` einen Fehllaut nach dem letzten Wort selbst (Funktion `valley_cut`, Hörprobe B der Ersteller:in): Nach einer Senke (höchstens 15 % der lautesten Stelle) folgt ein kurzer (höchstens 130 ms), leiser (höchstens 30 % der Spitze) Ausschlag mit höchstens 2 % der Energie; dann wird an der Senke geschnitten (30 ms Fade). Jeder Schnitt wird mit Satz, Stelle und Kürzung gemeldet („dip cut“). Mit `--no-dip-cut` bleibt der Schnitt aus. Ob dabei nie ein echter Laut fehlt, hört nur die Ersteller:in: Paare vorher und nachher in `.vibe/hoerprobe-schnitt/`, Liste unten.

## Hörliste

Sätze, die auf ein einsilbiges Wort enden und deshalb gezielt angehört werden sollen (die Stimme hängt dort leicht ein Ausklingen an): she-can-run, they-can-sing, we-can-swim, i-can-read, he-can-jump, you-can-swim (Seite 1); sophie-can-help-you, peter-can-see-us, ellie-can-see-them, amir-can-help-her, we-can-see-him, they-can-call-me (Seite 2); we-can-see-their-books, they-can-see-our-ball, you-can-see-my-book, we-can-see-your-bag (Seite 3); amir-can-see-his-bag, peter-can-see-his-bag, he-can-see-her-and-her-bag (Seite 4). Zweisilbig enden: i-can-see-your-jacket, they-can-see-my-jacket, ellie-can-call-her-brother, peter-can-help-his-sister, ellie-can-help-her-brother. Zuerst hören: die Sätze auf run, jump und you (zuvor mit Fehllaut beanstandet: we-can-run, he-can-run, we-can-jump, we-can-call-you; diese Sätze gibt es so nicht mehr).

Mit Schnitt an der Senke (`valley_cut`; die zweisilbigen Enden zuerst anhören): ellie-can-call-her-brother, ellie-can-help-her-brother, i-can-see-your-jacket, they-can-see-my-jacket, peter-can-see-his-bag, you-can-see-my-book, we-can-see-your-bag, peter-can-see-us, they-can-call-me. Gefällt bei einer Datei die Fassung ohne Schnitt besser, mit `--no-dip-cut` neu erzeugen und hier vermerken.
