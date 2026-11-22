# Trockenlauf der Regel „Fehllaut nach der letzten Senke schneiden“

App englisch-pronomen, 24 Hörsätze (bf_emma). Nichts wurde in `src/audio/` geschrieben. Bericht erzeugt mit `dry_run.py` (Rohsignal der Stimme, wie das Skript beim Erzeugen).

| Datei | Satz | Schnitt | Senke bei | Fehllaut-Länge | Ausschlag | Energie |
|---|---|---|---|---|---|---|
| ellie-can-call-her-brother.mp3 | Ellie can call her brother. | ja | 1350 ms | 60 ms | 0.2 | 0.52 % |
| peter-can-help-his-sister.mp3 | Peter can help his sister. | nein (Wächter) | 1300 ms | 240 ms | 0.64 | 10.84 % |
| amir-can-see-his-bag.mp3 | Amir can see his bag. | nein (Wächter) | 1010 ms | 320 ms | 1.0 | 20.17 % |
| ellie-can-help-her-brother.mp3 | Ellie can help her brother. | ja | 1270 ms | 50 ms | 0.19 | 0.4 % |
| peter-can-see-his-bag.mp3 | Peter can see his bag. | ja | 1260 ms | 40 ms | 0.13 | 0.22 % |
| he-can-see-her-and-her-bag.mp3 | He can see her and her bag. | nein (Wächter) | 1110 ms | 320 ms | 0.97 | 20.46 % |
| i-can-see-your-jacket.mp3 | I can see your jacket. | ja | 1360 ms | 80 ms | 0.25 | 0.63 % |
| we-can-see-their-books.mp3 | We can see their books. | nein (Wächter) | 1150 ms | 110 ms | 0.36 | 1.62 % |
| they-can-see-our-ball.mp3 | They can see our ball. | nein (Wächter) | 820 ms | 320 ms | 0.61 | 23.85 % |
| you-can-see-my-book.mp3 | You can see my book. | ja | 1150 ms | 100 ms | 0.25 | 0.52 % |
| we-can-see-your-bag.mp3 | We can see your bag. | ja | 1120 ms | 60 ms | 0.1 | 0.19 % |
| they-can-see-my-jacket.mp3 | They can see my jacket. | ja | 1360 ms | 80 ms | 0.24 | 0.62 % |
| sophie-can-help-you.mp3 | Sophie can help you. | nein (Wächter) | 940 ms | 230 ms | 0.44 | 12.12 % |
| peter-can-see-us.mp3 | Peter can see us. | ja | 1000 ms | 120 ms | 0.24 | 0.97 % |
| ellie-can-see-them.mp3 | Ellie can see them. | nein (Wächter) | 770 ms | 240 ms | 0.7 | 16.56 % |
| amir-can-help-her.mp3 | Amir can help her. | nein (Wächter) | 890 ms | 260 ms | 0.64 | 10.9 % |
| we-can-see-him.mp3 | We can see him. | nein (keine Senke mit Ausschlag) | | | | |
| they-can-call-me.mp3 | They can call me. | ja | 980 ms | 30 ms | 0.08 | 0.23 % |
| she-can-run.mp3 | She can run. | nein (keine Senke mit Ausschlag) | | | | |
| they-can-sing.mp3 | They can sing. | nein (Wächter) | 500 ms | 350 ms | 0.64 | 32.49 % |
| we-can-swim.mp3 | We can swim. | nein (Wächter) | 490 ms | 380 ms | 1.0 | 50.21 % |
| i-can-read.mp3 | I can read. | nein (Wächter) | 800 ms | 130 ms | 0.37 | 3.72 % |
| he-can-jump.mp3 | He can jump. | nein (Wächter) | 830 ms | 120 ms | 0.25 | 2.1 % |
| you-can-swim.mp3 | You can swim. | nein (Wächter) | 490 ms | 380 ms | 1.0 | 50.86 % |

**9 von 24 Dateien würden sich ändern (38 %).**
Fehllaut-Länge = Dauer vom Schnitt bis zum letzten hörbaren Rest (über 8 % der Spitze); danach folgt nur noch das Ausklingen, das schon jetzt abgeschnitten wird.

Die vier beanstandeten Sätze (We can run. / He can run. / We can jump. / We can call you.) werden von der Regel geschnitten (geprüft, Ausschlag 0,19 bis 0,23). Sie stehen nicht mehr in der App.

Geschnitten würden: ellie-can-call-her-brother, ellie-can-help-her-brother, peter-can-see-his-bag, i-can-see-your-jacket, you-can-see-my-book, we-can-see-your-bag, they-can-see-my-jacket, peter-can-see-us, they-can-call-me.
