# regen_audio.py mit Fehllaut-Erkennung (Vorschlag)

Auf Wunsch der Ersteller:in (Hörprobe B gefiel): Der Fehllaut nach dem letzten Wort wird erkannt und geschnitten.

## Regel (`valley_cut` in `regen_audio.py`)

Hüllkurve in Fenstern von 10 ms, auf die lauteste Stelle normiert; `last` ist das letzte Fenster mit mindestens 8 % (dort endet schon bisher der Schnitt des Ausklingens).

1. Suche in den letzten 400 ms vor `last` die **letzte Senke** `v`: lokales Minimum mit höchstens 15 % der Spitze.
2. Danach folgt ein **Ausschlag** von mindestens dem 1,4-fachen der Senke.
3. Schutz gegen das Abschneiden echter Silben, alle drei müssen gelten:
   - der Rest nach der Senke ist **kurz**: höchstens 130 ms bis `last`;
   - der Ausschlag ist **leise**: höchstens 30 % der Spitze (eine echte Silbe ist lauter; die Fehllaute der vier Sätze lagen bei 19 bis 23 %);
   - der Rest trägt **wenig Energie**: höchstens 2 % der Datei.
4. Dann wird an der Senke geschnitten (Mitte des Fensters), 30 ms Fade, keine Stille angehängt (Variante B).
5. Sonst gilt wie bisher der Schnitt des Ausklingens (Schwelle 8 %).

Jeder Schnitt wird mit Satz, Stelle, entfernten ms und Prozent der Dauer gemeldet („dip cut: …“). Mit `--no-dip-cut` (Standard: Schnitt an) bleibt er aus; mit `DRY=1` schreibt das Skript keine Dateien.

## Dateien

- `regen_audio.py`: fertiges Skript (statt `.agents/skills/app-content/scripts/regen_audio.py`).
- `dry_run.py`: Trockenlauf über `audio-texte.json`, schreibt `dry_run.json`. Aufruf im Ordner der App: `python .vibe/regen-audio-neu/dry_run.py .vibe/regen-audio-neu/audio-texte.json`.
- `bericht.md`, `dry_run.json`: Ergebnis für diese App.
- `audio-texte.json`: Sätze und Dateinamen.

## Grenze

Das Skript kann nicht wissen, ob eine Senke ein Fehllaut oder der Übergang zwischen zwei Silben ist. Die Wächter (kurz, leise, wenig Energie) sind aus den Hörproben der vier Sätze und 24 Hörsätzen abgeleitet. Ein Mensch hört die geschnittenen Dateien einmal gezielt an, vor allem Wörter mit zweiter Silbe am Satzende (brother, jacket).
