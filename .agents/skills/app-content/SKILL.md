---
name: app-content
description: Use for any content work in this app - researching, writing, extending, correcting or reviewing its competencies, chapters, pages, rounds, questions, exercises, figures, terms or sources. This app's own content decisions; they take precedence over the generic lernapps content skills. Load it before you change any content.
---

# Content guide of this app

Pronomen: I, me, my, mine, myself. Explainer (Strang-App `englisch/grammatik`, Stufe 5-6 und 7-8, Sprache Deutsch). Auftrag: Issue lernapps/apps#471. Gebaut sind Kapitel 1 „Wer? Wen? Zu wem?“ (Stufe 5-6, `pronomen-1`) und Kapitel 2 „mine, myself und each other“ (Stufe 7-8, `pronomen-2`).

## Curriculum

Englisch als erste Fremdsprache, Klasse 5-6. Kein Lehrplan: Reihenfolge und Bausteine kommen aus der Lernlandkarte `https://lernapps.net/apps/map/englisch.json` (Fokus `competency`). Vorwissen: Hello, Millbrook! (noun, verb, adjective, sentence, tense). Nicht hier: Demonstrativbegleiter, some/any (#475), Relativpronomen (#481), Formen von to be (#472); mine/yours, myself, each other kommen in Kapitel 2.

## Competencies

Kapitel `pronomen-1` („Wer? Wen? Zu wem?“), vier Seiten:

1. `personalpronomen`: Ich kann die Personalpronomen als Subjekt (I, he, they) und als Objekt (me, him, them) richtig verwenden. → `pronomen-1/wer-tut-es` (Subjekt), `pronomen-1/wen-trifft-es` (Objekt)
2. `possessivbegleiter`: Ich kann mit my, your, his, her, its, our und their sagen, wem etwas gehört. → `pronomen-1/my-your` (my, your, our, their), `pronomen-1/his-her` (his, her, its)

Beide Kompetenzen sind Lücken der Karte, `personalpronomen` hat keine Voraussetzung, `possessivbegleiter` verlangt `personalpronomen` (steht früher). Kein `ahead`, keine Wiederholungsseite. Übungs-IDs: Präfix = Seite (`wer-…`, `wen-…`, `my-…`, `his-…`). Je Seite: `<p>-start` (single-choice im Einstieg), `-zuordnen` (matching, Seiten 1 bis 3), `-waehlen-1`, `-waehlen-2` (zwei `single-choice` mit Satz und Lücke „___“, eine Meldung `info` je Option; die Nummern sind nicht durchgehend: wer 1 und 3, wen 2 und 3, my 1 und 3, his 1 und 2), `-schreiben` (write mit `mistakes`), `-falsch`/`-it` (true-false), `-hoeren` (Diktat), `-tabelle` (Tabelle ausfüllen), `-nachsprechen` (speaking-task); Seite 2 zusätzlich `wen-ordnen` (ordering), Seite 3 `my-luecke` (gap), Seite 4 `his-gemischt` (write, zwei Sätze mit Pronomen aus drei Spalten) und `his-frei` (open-task). Selbsteinschätzung in `src/pronomen-1/chapter.yaml`: je Seite `<p>-waehlen-N` (wer 1, wen 2, my 1, his 2) und `-schreiben`, zusammen acht Übungen.

## Kapitel 2 (Stufe 7-8, `pronomen-2`)

- Kompetenzen: `possessivpronomen` → `pronomen-2/mine-yours` (Chat, Ich kann die Possessivpronomen mine, yours, his, hers, ours und theirs verwenden), `reflexivpronomen` → `pronomen-2/myself` (Tagebuch, Vergleich mit dem deutschen „sich“), `each-other` → `pronomen-2/each-other` (Dialog, Unterschied zu themselves). Voraussetzungen stehen in Kapitel 1; keine Wiederholungsseite, kein `ahead`.
- Seitenaufbau (neu, Abschnitts-IDs): `einstieg` (Vorwissen-Frage `<p>-start`, „Das kannst du danach“), `lesen` (Lesestück 150 bis 300 Wörter: nummerierte Zeilen in zwei `text`-Blöcken, Wörter am Rand als `definition`-Blöcke), `verstehen` (drei Stufen: Verstehen `-text-1/2`, Belegen mit der Zeile `-text-3/4` als `single-choice` mit Zeilennummern, Meinung `-text-5` als `open-task`), `neu` (Poster-Ausschnitt mit drei Spalten, Merke), `uebung` (drei `single-choice` `-waehlen-N`, `matching` oder `ordering`, `-korrigieren`, `-schreiben`, `-falsch`, `-hoeren`, `-tabelle` zuletzt), `anwenden` (`-nachsprechen`, Schreibauftrag `-schreiben-frei`), `weiter`. Die Seite `each-other` endet mit dem Rückblick auf Kapitel 2.
- Figuren: Sophie 13, Ellie 13, Amir 13, Peter 11 (zwei Jahre später, Sophie besucht Millbrook wieder; (guess)). Keine Szenenbilder, nur zwei Pfeil-Bilder: `images/pfeile-selbst.svg` (herself: Pfeil zurück; her: Pfeil zu einer anderen Person) und `images/pfeile-each-other.svg` (hin und her; themselves). Mrs Parker kommt nicht vor.
- Poster: Ausschnitt mit drei Spalten (Person, Mit Nomen, Ohne Nomen auf Seite 1; Person, Wer tut es?, Wer ist es selbst? auf Seite 2), weil sechs Spalten bei 360 px überlaufen; each other als Kasten (Merke) auf Seite 3.
- Wörter außerhalb des Grundwortschatzes: hoodie (erklärt). Das Randglossar jeder Seite ist ein Vokabelblock (`type: vocabulary`, Überschrift „Wörter am Rand“, Sprachen de → en, Einträge mit `target`, `source`, bei Verben `forms`, bei hurt und cut ein `example`); er ersetzt die früheren `definition`-Blöcke, die Wörter erscheinen dadurch nicht mehr im App-Glossar. Bei Kapitel 1 stehen die Wortlisten als Fließtext, nicht als Tabelle: unverändert.
- Quellen: Die Lesestücke sind eigene Texte ohne Fakten aus Wikipedia (die Abfrage antwortete mit HTTP 429, ungeprüft). Hörsätze neu mit `regen_audio.py`.
- Selbsteinschätzung `src/pronomen-2/chapter.yaml`: je Seite `-waehlen-N` und `-schreiben` (mine-waehlen-2, myself-waehlen-1, each-waehlen-1), sechs Übungen.

## Content structure

- Keine Einführung der Figuren auf den Seiten (Rückmeldung der Ersteller:in): kein Vorstellen mit Alter, Herkunft oder Verwandtschaft, kein Datum ohne Nutzen für die Aufgabe; eine Figur wird nur genannt, wo die Aufgabe sie braucht. Die Vorstellung steht einmal in der Einleitung der Startseite (`src/app.yaml`).

- Pfad: `src/pronomen-1/chapter.yaml`, Seiten `src/pronomen-1/<seite>.yaml`.
- Jede Seite hat dieselben Abschnitts-IDs: `einstieg` (Szene, erste leichte Aufgabe, „Das kannst du danach“), `neu` (Tabelle wächst, Kasten „Merke“), `uebung` (mindestens vier Übungen, leicht → schwer), `anwenden` (`speaking-task` oder `open-task`), `weiter` (nächster Schritt der Geschichte; Seite 4 mit Rückblick). Titel sagen, was der Abschnitt tut.
- Länge: höchstens 350 Wörter Text, höchstens 4 Textblöcke hintereinander, Bild oder Übung unter den ersten vier Blöcken.
- Geschichte: Sophie (11, blond, Zöpfe, grüne Jacke, aus Deutschland, wohnt bei den Parkers), Ellie Parker (11, roter Pferdeschwanz, rote Jacke), Peter Parker (9, kurze braune Haare, gelbe Jacke, Ellies Bruder), Amir (11, schwarze Locken, Brille, blaue Jacke), Mr Hill (Englischlehrer, graue Haare, braune Jacke), Mrs Parker (Ellies Mutter, Sophies Gastmutter; verbindliches Aussehen laut Konventionen: rote Haare #b5501e als Dutt, türkise Strickjacke #2a9d8f, Haut #f1cdb0; in dieser App nicht gezeichnet). Millbrook School, erfundene Schule in einer englischen Kleinstadt, Schultag beginnt 8:45. Geburtstage: Peter 5. Mai, Ellie 10. Juli, Amir 12. Oktober, Sophie 14. Oktober. Je Seite eine Szene mit kurzen Sätzen und Dingen aus dem Alltag.
- Alle Beispielsätze nutzen `can` mit einem Verb, damit sich das Verb nicht ändert (kein -s). Drei getrennte Sätze je Seite: Text, Kasten Merke und Bild nutzen andere Verben und Nomen als die Übungen, und die Hörsätze (Diktat, Nachsprechen) wieder andere (Regel: kein Satz doppelt, auch nicht mit getauschtem Pronomen, Namen, Verb oder Nomen). Seite 1: Übungen swim, run, sing, jump; Merke read, play, dance; Hören cook, write, draw. Seite 2: Übungen see, help, call; Text find; Merke hear. Seite 3: Übungen bag, jacket, ball, book; Text und Merke phone, hat, bike, dog. Seite 4: Übungen jacket, sister, brother, cat, ball; Text hat, bike; Merke hat, phone, dog; Hören pen, cap, bag. Wörter stehen vor den Übungen auf der Seite mit Bedeutung.
- Das wachsende Bild: Tabelle „Klassenzimmer-Poster · Pronomen“ (Seite 1: Person · Wer tut es?; Seite 2 + Wen trifft es?; Seite 3 + Zu wem gehört es? mit allen sieben Zeilen, für he, she, it steht dort „?“; Seite 4 füllt die Zellen; Zeilenkopf = deutsches Wort ich, du / ihr, er, sie (ein Mädchen), es, wir, sie (mehrere), `rowHeaders: true`). Seite 4 hat zusätzlich die Figur `images/his-her-person.svg` (Pfeile von der Person zu ihrem Hut: her hat bei Ellie, his hat bei Peter; die Beispiele mit Verwandten stehen im Text: Mrs Parker ist her mother für Ellie und his mother für Peter, nicht gezeichnet). Die Tabelle steht nicht direkt über der Übung, die sie beantwortet.

## Terminology

- Nie „Besitzer“ oder „Ding“, wenn es um Menschen geht (her mother, his sister): „die Person, zu der es gehört“; was dazugehört: „Person oder Sache“. Spalte 3 heißt „Zu wem gehört es?“ (Rückmeldung des Erstellers; im Issue stand „Wessen Ding?“). Bild `src/images/his-her-person.svg`.

- Anrede „du“; „Ausdruck“ (fester Ausdruck), nie „Wendung“. Britisches Englisch, kein deutsches Wort in einem englischen Satz.
- Fachbegriffe noun, verb, adjective, sentence, tense gelten. „Subjekt“ (wer tut es) und „Objekt“ (wen trifft es) werden auf den Seiten 1 und 2 erklärt, wo sie gebraucht werden; „Possessivbegleiter“ als „Wort, das sagt, wem etwas gehört“.
- Aussprache nur als Lesehilfe in deutscher Annäherung, betonte Silbe in Großbuchstaben, keine Lautschrift (gehört in #482).
- Englische Wörter immer mit deutscher Bedeutung beim ersten Auftreten; Übungen fragen nur Wörter ab, die vorher auf der Seite stehen.

## Exercise patterns

Von leicht zu schwer: wählen (`matching`, `single-choice`) → Lücken und Formen wählen (`language-task` mode `choice`/`gap`) → Tabelle ableiten (`language-task` mode `table`) → schreiben (`write`, Deutsch → Englisch, `mistakes`) → korrigieren → hören (Diktat) und nachsprechen.

- Person ↔ Pronomen zuordnen: `matching` (Seite 1).
- Pronomen wählen: zwei `single-choice` je Seite mit Satz und Lücke „___“, Wahlmöglichkeiten sind echte Lernerfehler mit eigener `info` (ein `language-task` mode `choice` zeigt seine `mistakes` nicht an, darum nicht verwenden, wenn die Meldung zählt).
- Tabelle ableiten (I – me – my): `language-task` mode `table`.
- Die Person, zu der es gehört, bestimmt his/her: `single-choice` (Seite 4, `his-waehlen-1` und `-2`) und `write`.
- Satz bauen: `ordering`.
- Hören/Nachsprechen: `language-task` mit `audio`, `speaking-task`; Audio: Stimme `bf_emma`, nur ganze Sätze, Dateien `src/audio/<satz-in-kleinbuchstaben>.mp3`.
- Je Fehlertyp eine Rückmeldung in `mistakes` oder `info`: I/me, he/him, his/her nach der Person oder Sache, die dazugehört, statt nach der Person, zu der sie gehört, its/it's.
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
- Audio: Die Stimme hängt an kurzen Sätzen ein Ausklingen an; alle Dateien entstehen mit `regen_audio.py` (im Ordner der App, mit dem Python der Audio-Umgebung `~/.cache/lernapps/audio/venv/bin/python`). Namen am Satzende zweisilbig (Sophie, Peter, Ellie). Hörsätze bleiben natürlich: Es wird kein Name nur wegen des Klangs angehängt. Das Ausklingen schneidet `regen_audio.py` ab (alle Sätze samt Dateinamen: `.agents/skills/app-content/audio-texte.json`; Aufruf `python regen_audio.py audio-texte.json "<Satz>"`). Zusätzlich schneidet `regen_audio.py` einen Fehllaut nach dem letzten Wort selbst (Funktion `valley_cut`, Hörproben der Ersteller:in): Nach einer Senke (höchstens 15 % der lautesten Stelle) folgt ein kurzer (höchstens 130 ms), leiser (höchstens 30 % der Spitze) Ausschlag mit höchstens 2 % der Energie; dann wird 40 ms hinter der Senke geschnitten (30 ms Fade), wenn dabei 20 bis 100 ms wegfallen. Jeder Schnitt wird mit Satz, Stelle und Kürzung gemeldet („dip cut“). Mit `--no-dip-cut` bleibt der Schnitt aus. Ob dabei nie ein echter Laut fehlt, hört nur die Ersteller:in: Paare vorher und nachher in `.vibe/hoerprobe-schnitt/`, Liste unten.

## Hörliste

24 Hörsätze (Dateien `src/audio/<satz>.mp3`, Sätze in `audio-texte.json`). Jede Seite: Diktat (`-hoeren`) und Nachsprechen (`-nachsprechen`).

- Seite 1: she-can-cook, they-can-write, we-can-draw (Diktat); i-can-cook, he-can-write, you-can-draw.
- Seite 2: sophie-can-help-you, peter-can-see-us, ellie-can-see-them; amir-can-help-her, we-can-see-him, they-can-call-me.
- Seite 3: i-can-see-your-jacket, we-can-see-their-books, they-can-see-our-ball; you-can-see-my-book, we-can-see-your-bag, they-can-see-my-jacket.
- Seite 4: ellie-can-find-her-pen, amir-can-find-his-cap, mr-hill-can-see-his-bag; sophie-can-find-her-cap, amir-can-see-his-pen, the-dog-can-find-its-bag.

Alle enden auf ein einsilbiges Wort, außer i-can-see-your-jacket und they-can-see-my-jacket (zweisilbig). Gezielt anhören: die Dateien mit Schnitt an der Senke (`valley_cut`): ellie-can-find-her-pen, amir-can-find-his-cap, the-dog-can-find-its-bag, i-can-see-your-jacket, you-can-see-my-book, we-can-see-your-bag, they-can-see-my-jacket, peter-can-see-us, she-can-cook, they-can-write, i-can-cook, he-can-write. Gefällt bei einer Datei die Fassung ohne Schnitt besser, mit `--no-dip-cut` neu erzeugen und hier vermerken.

Stand: Die Ersteller:in hat die Regel (Rand 40 ms, 20 bis 100 ms) gehört und für gut befunden („passt“). Das Skript liegt auch in `lernapps/start` unter `orchestrierung/audio/`. Die ersten vier beanstandeten Sätze (we-can-run, he-can-run, we-can-jump, we-can-call-you) gibt es nicht mehr.

### Hörliste Kapitel 2 (18 Hörsätze, nichts davon angehört)

- `mine-yours`: the-tickets-on-the-table-are-ours, is-this-ruler-yours, these-keys-are-his (Diktat); this-jacket-is-theirs, that-umbrella-is-hers, that-watch-is-mine (Nachsprechen).
- `myself`: i-bought-myself-a-new-phone, he-bought-himself-a-ticket, the-cat-cleaned-itself (Diktat); you-can-do-it-yourself, we-can-help-ourselves, help-yourselves-please.
- `each-other`: the-twins-know-each-other-well, do-you-see-each-other-often, the-boys-made-themselves-a-pizza; please-be-kind-to-each-other, the-girls-are-talking-to-each-other, they-can-do-it-themselves.
- Mit Schnitt an der Senke (`valley_cut`, gezielt anhören): the-tickets-on-the-table-are-ours, these-keys-are-his, this-jacket-is-theirs, he-bought-himself-a-ticket, the-cat-cleaned-itself, you-can-do-it-yourself, help-yourselves-please. Die meisten Sätze enden auf ein einsilbiges Wort; zweisilbig enden the-cat-cleaned-itself und the-boys-made-themselves-a-pizza (pizza).
