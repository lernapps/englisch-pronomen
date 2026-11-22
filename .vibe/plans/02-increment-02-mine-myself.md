---
# Read by the hooks, the review, the evals. Schema: @lernapps/tooling/guidance/plan-front-matter.v1.schema.json
# Written by `lernapps plan` and the hooks. Never change a key or a value by hand.
# Archetype, as in the app's first plan. Allowed values: explainer, interactive, quiz.
archetype: explainer
# Current phase. Allowed values: explore, plan, code, commit.
phase: code
# prePushFailures: failed pre-push runs of this increment, written by the hook.
prePushFailures: 0
# failedChecks: failed rules and runs, written by lernapps check and the hooks.
failedChecks: {}
---

# Increment: increment-02-mine-myself

<!--
For you, the assistant. One increment of a published app: new competencies, chapters, pages, rounds, questions, or a
correction. The process is in AGENTS.md; this plan holds the method.
- `npx --no -- lernapps plan next` prints the task to do now, `plan done` ticks it and prints the next one.
- You write only below Goal, Key decisions, Notes, Answers, Content method and Retrospective, in the creator's
  language. Delete the comment of a section once the section is filled.
- The first version's decisions stand: archetype, content method, content guide. Never change an earlier plan.
- Work on the branch `increment/<NN>-<short name>`. Until Commit everything is local: push nothing.
-->

*Started 2026-11-22. Explore, Plan, Code, Commit.*

## Goal

<!-- 1–2 sentences: what learners can do after this increment. -->

Kapitel 2 „mine, myself und each other“ (Stufe 7-8) ergänzt die Pronomen-Tabelle um zwei Spalten und übt die drei Bausteine Possessivpronomen, Reflexivpronomen und each other mit je einem Lesestück (Chat, Tagebuch, Dialog) von Sophie, Ellie, Peter und Amir.

## Key decisions

<!-- One line each: decision and reason. Your own choice without the creator: mark "(guess)". -->

- `scope`: ja, bleibt (der App-`scope` und jede Seite haben einen; neue Seiten bekommen eine, `src/app.yaml` wird um Kapitel 2 ergänzt).
- Poster-Tabelle ab Kapitel 2 als Ausschnitt (drei Spalten: Person, neue Spalte, Vergleichsspalte), weil sechs Spalten bei 360 px überlaufen. (guess)
- Wörter außerhalb des Grundwortschatzes: hoodie (erklärt, im Inhaltsführer).


## Notes

<!-- New competencies by chapter (ids of the strand), didactic approach, scope, sources and licences, open questions. -->

- Quelle des Auftrags: Issue #471 (Kapitel 2) und `konventionen.md`, Abschnitt 7 und 8 (aus `lernapps/start`, Branch `claude/exciting-shannon-vi3k3t`), geöffnet.
- Karte (englisch.json) gelesen: `possessivpronomen` (7-8, Schritt 1, requires possessivbegleiter), `reflexivpronomen` (7-8, Schritt 1, requires personalpronomen), `each-other` (7-8, Schritt 2, requires reflexivpronomen). Voraussetzungen stehen in Kapitel 1 dieser App: keine Wiederholungsseite nötig.
- Seiten (3, Reihenfolge nach requires): (1) `mine-yours` (possessivpronomen), (2) `myself` (reflexivpronomen, Vergleich mit dem deutschen „sich“), (3) `each-other` (each-other, Unterschied zu themselves). Kapitel `pronomen-2`, Titel der App danach wieder „Pronomen: I, me, my, mine, myself“.
- Jede Seite hat ein Lesestück (150 bis 300 Wörter, Randglossar, drei Aufgabenstufen Verstehen, Belegen mit Zeile, Meinung; zuletzt ein Schreibauftrag), danach die Übungen zum Baustein. Sorten: Chat-Verlauf der Figuren (Seite 1), Tagebucheintrag von Sophie (Seite 2), kurzer Dialog (Seite 3). Eigene Texte, keine Sätze aus fremden Quellen.
- Tabelle: zwei Spalten dazu: „Gehört es mir, ohne Nomen?“ (mine, yours, his, hers, ours, theirs; it hat keine Form, its bleibt) und „Wer ist es selbst?“ (myself, yourself, himself, herself, itself, ourselves, yourselves, themselves). each-other als eigener Kasten mit Pfeilen (hin und her), die Reflexiv-Pfeile gehen zur selben Person zurück.
- Wie Lernende hinkommen: Sie ergänzen die Muster selbst (my – mine, your – yours; hers statt her, ohne Apostroph), sehen Pfeile (selbe Person oder hin und her) und vergleichen deutsches „sich“ (sich treffen – meet, sich beeilen – hurry) mit dem Englischen. Fehlvorstellungen: mine's/yours' mit Apostroph, his mine, hisself/theirselves, I meet myself statt I meet, myself und each other verwechselt.
- Umfang: drin die drei Bausteine, alle acht Formen von -self/-selves. Draußen: emphatisches Reflexivpronomen (I did it myself) nur kurz als Beispiel, Relativpronomen (#481), some/any (#475), to be (#472). Sprache: Deutsch erklärt, Englisch britisch.
- Quellen: Die Wikipedia-Abfrage antwortete mit HTTP 429 (zu viele Anfragen), darum ist jede Faktenangabe aus Wikipedia **ungeprüft** und wird vorsichtig formuliert (nur Grundformen von Possessiv-, Reflexiv- und Reziprokpronomen, die schon der Lernlandkarte zu entnehmen sind). Kein Satz aus fremden Texten. VOA, Wikinews und African Storybook nicht geöffnet (nicht nötig: eigene Lesestücke).

- Neue Seitenart „Lesestück“ (Skills lernapps-explainer-design und lernapps-exercise-patterns gelesen, in dieser Sitzung bereits ganz): Abschnitt `lesen` mit Vorwissen-Frage (`single-choice`), dem Text in Abschnitten (`text`-Blöcke mit nummerierten Zeilen), einer Tabelle „Wörter am Rand“ je Abschnitt als Randglossar (`table`: Wort, Bedeutung; höchstens eine kurze Tabelle je Seite, dazu die Poster-Tabelle: Prüfung gegen die Regel „höchstens eine kurze Wörtertabelle je Seite“ offen, Glossar dann als `definition`-Blöcke), danach drei Aufgabenstufen: Verstehen (`single-choice`, `true-false`), Belegen mit Zeile („Welche Zeile belegt …?“ als `single-choice` mit Zeilennummern), Meinung (`open-task`); zuletzt Schreib- oder Sprechauftrag (`open-task`, `speaking-task`). Textlänge 150 bis 300 Wörter; zählt nicht zu den 350 Wörtern Erklärtext. Keine Komponente nötig (`prefer-built-in-block`).
- Didaktik je Kompetenz: possessivpronomen: Lesestück Chat „Wem gehört die Jacke?“, Lernende entdecken my → mine, your → yours aus dem Chat und ergänzen die Spalte, Besonderheit: hers, ohne Apostroph, it hat kein Possessivpronomen. reflexivpronomen: Tagebuchtext, Pfeil zur selben Person (myself), Vergleich „sich treffen – meet“, „sich beeilen – hurry“, Lernende ordnen deutsche Verben mit und ohne englisches Reflexivpronomen. each-other: Dialog zweier Figuren, Pfeile hin und her, Unterschied themselves/each other mit Satzpaaren.
- Offen: Randglossar als Tabelle oder `definition`-Blöcke je nach Regel zur Wörtertabelle (Entscheidung beim Bau der Musterseite).
- Korrektur: Beim Weiterschalten habe ich vier Slice-Aufgaben abgehakt, bevor sie gemacht waren (Schleife mit `plan done`). Das Abhaken lässt sich nur von Hand zurücknehmen (verboten: `plan-file`); darum stehen die vier Slices als neue Aufgaben („really do it“) hinter den abgehakten. Die abgehakten sind erst mit den neuen erledigt.

## Explore

<!--
- All content questions belong here; Plan maps the answers onto the app. Ask; write no code.
- Skip what earlier answers or the app already tell. At most 2 questions per message, one topic each.
-->

### Tasks

- [x] Read the README of the archetype's template (its path is in skill `lernapps-app`): what the app can do now.
      Tell the creator what is new, if it matters for this increment.
- [x] Load the content guide `.agents/skills/app-content/SKILL.md` and read the earlier plans in `.vibe/plans/`: what
      the app teaches, how its content is made, what is open.
- [x] Interview, one topic per question, the creator's words under "Answers": which competencies, chapters or rounds,
      for which school years; hurdles and examples; the amount; any change of look and feel or of terms. No answer:
      ask once more, then write your assumption with "(guess)".
- [x] Load skill `lernapps-content-research`. Research what the content guide does not cover. Write under "Notes":
      the new competencies by chapter with their ids, the sources you opened.
- [x] Write under "Notes" the didactic approach per competency and the scope (in, out, data range).
- [x] The increment needs a kind of content the guide does not cover (a new page structure, screen, component or kind
      of exercise): load skills `lernapps-explainer-design` and `lernapps-exercise-patterns`. Else skip this task.
- [x] **Checkpoint:** research. Show in plain words: the new competencies by chapter, the didactic approach, the
      scope, every "(guess)", the sources and what is unchecked. Stop and wait. Changes: change them, then ask again.
      Creator: Ja, der Schnitt passt (3 Seiten, Lesestück je Seite); Randglossar als definition-Blöcke, wenn die Wörtertabellen-Regel greift; Lesestücke ohne ungeprüfte Wikipedia-Fakten (Orchestrator)

### Answers

<!-- The creator's answers, in their words, one bullet each. -->

- Competencies, chapters, school years: Kapitel 2 mit possessivpronomen, reflexivpronomen, each-other, Stufe 7-8 (Issue #471; Antwort der Orchestrator-Session in der Rolle der Ersteller:in).
- Hurdles: Muster my – mine, your – yours; sich treffen – meet; myself gegen each other; Apostroph bei Possessivpronomen.
- Amount: drei Seiten mit je einem Lesestück und Übungen.
- Look and feel, terms: wie Kapitel 1; „Ausdruck“, nie „Wendung“; Spalte „Zu wem gehört es?“ aus Kapitel 1 bleibt, neue Spalten mit eigener Frage. (guess für die Fragen der neuen Spalten)
- Figuren: Sophie 13 bis 14, Chats und kurze Dialoge (Konventionen, Abschnitt 8); (guess) Sophie besucht Millbrook wieder, Sophie 13, Ellie 13, Peter 11, Amir 13.


## Plan

<!--
- Map the new content onto the app with the guide's patterns. The creator confirms the plan in one read.
- After the yes you work on your own.
-->

### Tasks

- [x] Load skill `lernapps-content-growth`. Add the tasks of Code as slices, one per competency, in the guide's
      order, one call each: `npx --no -- lernapps plan add --at slices "<task>"`. Say in each which sub-agent may
      write it in parallel, if any.
- [x] Write "Content method": the guide's patterns, figures and components per slice. Anything new: map it as skill
      `lernapps-explainer-design` says, and say why the guide's patterns do not fit.
- [x] Draw a sketch of each new component or interactive exercise, in `.vibe/sketches/`.
- [x] Show the creator, short: goal, new competencies by chapter, slices; in plain words what learners see and do and
      what is new. At most 2 questions.
- [x] **Checkpoint:** confirm the plan and the content method. Stop and wait for an explicit yes. Changes: change
      them, then ask again.
      Creator: Ja, Plan bestätigt (Orchestrator)

### Content method

**Aufbau.** Kapitel `pronomen-2` („mine, myself und each other“, Stufe 7-8) mit den Seiten `mine-yours`, `myself`, `each-other` in `src/pronomen-2/`, eingetragen in `src/app.yaml` unter `chapters` nach `pronomen-1`. Abschnitts-IDs je Seite: `einstieg` (Vorwissen-Frage, „Das kannst du danach“), `lesen` (Lesestück), `verstehen` (drei Stufen), `neu` (Poster-Tabelle mit den zwei neuen Spalten, Kasten Merke), `uebung` (mindestens vier, leicht → schwer), `anwenden` (Schreib- oder Sprechauftrag), `weiter`. Kein Bild, wo es nichts zeigt: Bilder nur für die Pfeile.

**Lesestück (neue Seitenart, nur eingebaute Blöcke).** 150 bis 300 Wörter, eigener Text; Chat-Verlauf (Seite 1), Tagebucheintrag (Seite 2), kurzer Dialog (Seite 3) als `text`-Blöcke in Abschnitten mit nummerierten Zeilen (Markdown-Liste, `**Name:**` je Zeile). Randglossar als `definition`-Blöcke (ein Block je schwerem Wort, Wort + Bedeutung), da die Regel „höchstens eine kurze Wörtertabelle je Seite“ die Poster-Tabelle schon belegt. Vorwissen-Frage vor dem Text (`single-choice`). Aufgaben in drei Stufen: Verstehen (`single-choice`, `true-false`), Belegen mit Zeile (`single-choice`: „Welche Zeile zeigt …?“, Antworten sind Zeilennummern), Meinung (`open-task` mit `points`). Das Lesestück zählt nicht zu den 350 Wörtern Erklärtext; höchstens ein Lesestück und etwa 25 Items je Seite. Hörsätze (ganze Sätze) nur kurze Abschnitte, nie das ganze Stück.

**Die wachsende Tabelle** „Klassenzimmer-Poster · Pronomen“ (wie Kapitel 1): Seite 1 + Spalte „Gehört es mir, ohne Nomen?“ (my → mine, your → yours, his → his, her → hers, its → (keine Form), our → ours, their → theirs), Seite 2 + Spalte „Wer ist es selbst?“ (myself, yourself, himself, herself, itself, ourselves, yourselves, themselves), Seite 3 behält beide Spalten (`each other` als Kasten mit Pfeilen). Zeilenkopf wie in Kapitel 1 (deutsche Wörter). Höchstens eine Wörtertabelle je Seite, Übungs-Tabellen zählen als Übung.

**Figuren (nur Pfeile).** `src/images/pfeile-selbst.svg`: Sophie mit Pfeil zu sich selbst zurück (myself), Ellie mit Pfeil zu sich zurück (herself); `src/images/pfeile-each-other.svg`: Pfeile zwischen Ellie und Amir hin und her (each other). Figuren aus den bekannten Definitionen, Sophie 13 bis 14 wie bei den Lernenden altern (gleiche Haare, Zöpfe, Jacke); `alt` nennt, was gezeigt wird, nie die Lösung. Mrs Parker nicht gezeichnet (verbindliches Aussehen im Inhaltsführer).

**Muster je Kompetenz.** possessivpronomen: Muster ergänzen (`language-task` mode `table`), Auswahl `single-choice` mit `info` je Option (mine/my, yours/your), Schreiben (`write` mit `mistakes`: mine's, yours', hers/her's), Korrigieren, Hören. reflexivpronomen: Verben mit und ohne Reflexivpronomen (`matching` deutsches „sich“-Verb ↔ englisches Verb: sich treffen – meet, sich beeilen – hurry, sich setzen – sit down, sich freuen – be happy, aber: sich verletzen – hurt oneself), Auswahl `single-choice` (myself/me), Schreiben (`write`, I meet myself falsch). each-other: Satzpaare `single-choice` (themselves/each other), `ordering` (Satz bauen), Schreiben (`write`). Alle Auswahlübungen als `single-choice` mit `info` je Option (nicht `language-task` mode `choice`, dessen `mistakes` die Laufzeit nicht zeigt).

**Regeln aus Abschnitt 7 (gelten).** Kein Hörsatz (auch nicht mit getauschtem Pronomen, Namen, Verb oder Nomen) in Text, Merke, Bild oder einer anderen Übung derselben Seite; die Lösung einer Übung steht nicht im Text, Bild oder Poster direkt darüber; Distraktoren sind echte Lernerfehler mit eigener Meldung; mindestens vier Übungen je Seite mit sichtbarer eigener Meldung; Hörliste im Inhaltsführer, nichts Ungehörtes als „geprüft“; Audio mit `regen_audio.py` (Regel gegen den Fehllaut, Standard an); „Ausdruck“, nie „Wendung“; Spaltenfrage „Zu wem gehört es?“ aus Kapitel 1; „die Person, zu der es gehört“, nie „Besitzer“.

**Selbsteinschätzung** (Skill `lernapps-explainer-self-assessment`) für Kapitel 2: je Seite zwei Übungen (eine `single-choice`, ein `write`), die ohne Lesestück verständlich sind. **Wie ein späterer Agent weitermacht:** Seiten nach diesem Muster, Tabelle um Spalten ergänzen, Inhaltsführer folgt.

## Code

<!--
- Build locally on the branch, on your own. After each task: `plan done`, then one commit with the work and this
  plan. The hooks check each commit; a failing check is fixed from its message, as skill `lernapps-cli` says.
- What you cannot decide: choose, write it under "Key decisions" with "(guess)", go on.
- The creator asks for a change: say your reading in one sentence first.
-->

### Tasks

- [x] `git switch -c increment/<NN>-<short name>` from `main`. Commit this plan on it.
- [x] Load skill `lernapps-cli`. Update the app as its section "Update" says. Commit the update alone and fix its
      findings before any content. The update replaces the `lernapps-*` skills: read again those you use.
- [x] Load skill `lernapps-explainer` and the content guide.
- [x] Load skill `lernapps-content-questions`. Read whole, with your file tool:
      `.agents/skills/lernapps-explainer/references/blocks.md` and
      `.agents/skills/lernapps-explainer/references/exercises.md`. A foreign language: also
      `references/language-tasks.md` in the same folder. A component in the plan: also `references/components.md`.
- [x] Decide whether the app needs `scope`, as "`scope`" in
      `.agents/skills/lernapps-explainer/references/structure.md` says. Write the choice under "Key decisions".
- [x] Slice 1 (pattern page, me alone): chapter pronomen-2 in src/app.yaml and chapter.yaml, page mine-yours (possessivpronomen): chat Lesestück with Randglossar as definition blocks, three task levels, exercises, audio
- [x] Slice 2 (me alone, no sub-agent: shares chapter.yaml): page myself (reflexivpronomen): diary Lesestück, arrows to the same person, German sich versus English, exercises, audio
- [x] Slice 3 (me alone): page each-other (each-other): dialogue Lesestück, arrows back and forth, themselves versus each other, exercises, audio
- [x] Slice 4 (me alone): table with two new columns on the pages, app title back to Pronomen: I, me, my, mine, myself, selfAssessment of chapter 2, content guide, audio list, conventions of section 7
- [ ] Slice 1 (really do it; the earlier tick was a mistake of mine): page mine-yours with chapter pronomen-2, Lesestück chat with Randglossar, three task levels, exercises, audio; commit
- [ ] Slice 2 (really do it): page myself with diary Lesestück, arrows to the same person, sich versus English, exercises, audio; commit
- [ ] Slice 3 (really do it): page each-other with dialogue Lesestück, arrows back and forth, themselves versus each other, exercises, audio; commit
- [ ] Slice 4 (really do it): app title Pronomen: I, me, my, mine, myself, selfAssessment of chapter 2, content guide, audio list, section 7 conventions; commit
<!-- tasks: slices (8 added): one per competency, as written in Plan -->
- [ ] **Checkpoint:** the pattern page, after the first slice. A slice in a pattern the app already has: show it to
      the creator and go on. A new pattern: load skill `lernapps-learner-check`, do its learner check, fix what it
      finds, then ask the creator whether the others may follow it, and wait.
- [ ] Update the content guide so that it describes the app as it is now (`app-content-matches`).
- [ ] Run `npx --no -- lernapps check` until it passes.
- [ ] Look at every changed screen, at 360 px and on a desktop, as "Look at the app" of skill `lernapps-cli` says.

## Commit

<!--
- Publish with the creator's yes. A push to `main` publishes.
- Open the pull requests (to `main`, to the catalog) without asking: they publish nothing.
-->

### Tasks

- [ ] If pages or exercises changed, load skill `lernapps-explainer-self-assessment` and update the self-assessment
      as it says. Commit.
- [ ] Load skill `lernapps-github`. Push the branch, open the preview pull request and see its checks to green, as it
      says.
- [ ] **Checkpoint:** publish. Show what the increment adds and the preview link. Ask whether it may go online. Stop
      and wait for the yes.
- [ ] Load skill `lernapps-commit`. Publish as skill `lernapps-github` says: the pull request squash-merged into
      `main`, the run of `Pages` watched to its end.
- [ ] Open the address the job `deploy` printed and confirm the new content. Never use a derived address.
- [ ] The app is listed and its entry changes (school years, summary): load skill `lernapps-listing` and write the
      changed entry. Else skip this task.
- [ ] Fill the retrospective.
- [ ] Commit this plan on `main` and push it. A push of only `.vibe/` publishes nothing.
- [ ] **Checkpoint:** list. The entry changed: open the pull request to the catalog as skill `lernapps-listing`
      says, without asking first, see it to "bestanden", then show the creator the pull request and its result. The
      entry did not change: tell the creator that the catalog updates the app by itself.
- [ ] If the plan changed since its last push, commit it on `main` and push again.

## Retrospective

<!-- At the end of Commit. Facts, short, no names. Read by review and evals. -->

### Phases reached

<!-- Last phase completed, checkpoints passed. E.g. "commit; confirmed, published". -->

### Creator turns after the plan

<!-- Number of creator messages after the confirmation, topic of each. Target: at most 3. -->

### Where I had to guess

<!-- Each gap in plan, skills, content guide, messages or answers, and your choice. "None" if none. -->
