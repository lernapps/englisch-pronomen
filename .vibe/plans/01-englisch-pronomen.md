---
# Read by the hooks, the review, the evals. Schema: @lernapps/tooling/guidance/plan-front-matter.v1.schema.json
# Written by `lernapps plan` and the hooks. Never change a key or a value by hand.
# Archetype, null until chosen in Explore. Allowed values: explainer, interactive, quiz.
archetype: explainer
# Current phase. Allowed values: explore, plan, code, commit.
phase: code
# prePushFailures: failed pre-push runs, written by the hook.
prePushFailures: 0
# failedChecks: failed rules and runs, written by lernapps check and the hooks.
failedChecks: {}
---

# Plan: englisch-pronomen, first version

<!--
For you, the assistant. The process is in AGENTS.md; this plan holds the method.
- `npx --no -- lernapps plan next` prints the task to do now, `plan done` ticks it and prints the next one.
- You write only below Goal, Key decisions, Notes, Answers, Entry draft, Content method and Retrospective, in the
  creator's language. Delete the comment of a section once the section is filled.
- Work on the branch `work`, locally: push nothing before Commit.
-->

*Started 2026-11-21. Explore, Plan, Code, Commit.*

## Goal

<!-- 1–2 sentences: what learners do, what they learn. -->

## Key decisions

<!-- One line each: decision and reason. Archetype first. Your own choice without the creator: mark "(guess)". -->

- Archetyp: explainer (Format 2). Grund: Lernende brauchen Erklärseiten mit Tabelle und Szenen, dazwischen Übungen; kein Spiel, kein Timer nötig. Kann: Text, Tabellen, Figuren, Sprachaufgaben (choice/gap/table/write), Audio mit bf_emma, Vue-Komponenten fürs Ziehen. Kann nicht: Sprache bewerten, Spiel, eigene Farben.
- Strang-App `englisch/grammatik`, nur Kapitel 1 (Stufe 5-6); Kapitel 2 als Inkrement.
- `scope`: ja, in `src/app.yaml` und auf jeder Seite, weil Seite 4 eine `open-task` hat (der Tutor beurteilt sie nach dem `scope`).


## Notes

- Karte gelesen (englisch.json, explainerFocus: competency). Kapitel 1 deckt: `personalpronomen` (Stufe 5-6, Schritt 1, öffnet 103, keine Voraussetzungen) und `possessivbegleiter` (5-6, Schritt 2, öffnet 1, requires personalpronomen). Beide liegen im Explainer, daher keine Sammel-Wiederholung nötig (keine Voraussetzung von außen). Kapitel 2 (possessivpronomen, reflexivpronomen, each-other; 7-8) kommt später.
- Strang: englisch/grammatik.
- Üben (Muster Fremdsprachen): Wahl einer Form (choice mit distractors) → Lücken (gap) → Formen in der Tabelle (table) → Wort schreiben (write) → Zuordnen der Wörter in Spalten (Ziehen) → Übersetzen. Von leicht zu schwer, je Fehlertyp eine Rückmeldung (I/me, he/him, his/her nach Besitzer).
- Hörübungen mit bf_emma (Skill lernapps-audio), Sprechaufgabe möglich.
- Quellen (nur Fakten, keine Sätze; CC BY-SA, im Inhaltsführer unter "Sources"): https://en.wikipedia.org/wiki/Personal_pronouns_in_English (Titel "Personal pronouns in English", Einleitung geöffnet, verified); https://en.wikipedia.org/wiki/Possessive_determiner (Titel "Possessive determiner", verified: my, your, his, her, its, our, their; mine/yours gehören nicht dazu, sie stehen in Kapitel 2). Klexikon/de.wikipedia nicht geöffnet (ungeprüft, nicht benutzt). Kein Lehrplan nötig (Strang-App, die Karte gibt die Reihenfolge).
- Kompetenzen Kapitel 1: personalpronomen („Subjekt I/he/they und Objekt me/him/them“), possessivbegleiter („my, your, his, her, its, our, their“).
- Wie Lernende hinkommen: Sie ziehen Wörter in die Spalten der Tabelle (Wer tut es? Wen trifft es? Wessen Ding?) und entdecken das Muster (I – me – my) selbst. Fehlvorstellungen: „me am hungry“, „him is“, „I like he“ (Subjekt/Objekt verwechselt); his/her nach dem Ding statt nach dem Besitzer (Deutsch: seine/ihre nach dem Ding); its mit it's verwechselt; you singular/plural.
- Umfang: drin: I, you, he, she, it, we, they; me, you, him, her, it, us, them; my, your, his, her, its, our, their; Wortschatz aus Alltag (Familie, Schule, Tiere, Sachen). Draußen: mine/yours, myself, each other (Kapitel 2), Demonstrativa/some/any (#475), Relativpronomen (#481), to be (#472). Sprachen: Erklärung Deutsch, Beispiele britisches Englisch. Audio bf_emma.
- Seitenschnitt Kapitel 1 "Wer? Wen? Wessen?" (4 Seiten, Reihenfolge nach requires; keine Voraussetzung von außen, keine Wiederholungsseite, kein `ahead`): (1) `wer-tut-es` – personalpronomen, Subjekt (I, you, he, she, it, we, they; Tabelle Spalte 1); (2) `wen-trifft-es` – personalpronomen, Objekt (me, you, him, her, it, us, them; Spalte 2); (3) `my-your` – possessivbegleiter, my, your, our, their (Spalte 3, Muster I – me – my); (4) `his-her` – possessivbegleiter, his, her, its (Besitzer entscheidet, Bild zum Unterschied zum Deutschen) mit Schlussübung über die ganze Tabelle. Kapitelende: Rückblick auf die vollständige Tabelle. Seiten 3 und 4 teilen die Kompetenz possessivbegleiter (eine Kompetenz, zwei Seiten, weil groß).
- Kompetenz-Zeilen: personalpronomen: erst sortieren die Kinder Wörter in die Spalten, dann leiten sie ab, welche Form nach Verb (Subjekt) bzw. nach Verb/Präposition (Objekt) steht; Rückmeldung fängt I/me, he/him und "Me am…". possessivbegleiter: sie sehen die Reihe I–me–my und ergänzen die Muster selbst; Rückmeldung fängt his/her nach dem Ding (deutsches Denken), its/it's und you/your.

## Explore

<!--
- Find out what the app teaches, for whom, how much and how it looks. Ask; write no code, run no `create`.
- An answer counts only in the creator's words under "Answers". At most 2 questions per message, one topic each.
-->

### Tasks

- [x] Check the start: the folder `.agents/skills/lernapps-app` exists (else stop and tell the creator that the folder
      was not started with `init`), and `git branch --show-current` prints `work` (else `git switch -c work`).
- [x] Load skill `lernapps-app`. Tell the creator in two sentences what a lernapps app is and where it will live: at
      their own address, free and public, and once listed as a copy on lernapps.net. Say that the technical part
      (GitHub) comes at the end and that you do it.
- [x] Interview: ask the topics "Goal" and "Learners" of "Answers".
- [x] Load skill `lernapps-map-assignment` and read the learning map of the subject as it says. The creator brings
      the content themselves (material, a word list, the pages): note under "Notes" which competencies of the map it
      covers. Else write the skill's assignment, with its story; the creator's yes answers the topics Content and
      Amount. A subject without a map: skip this task and say so.
- [x] Load skill `lernapps-exercise-patterns` and read its reference for the subject. Note under "Notes" how learners
      will practise what the goal names.
- [x] Choose the archetype as skill `lernapps-app` says: read the README of each archetype in question, then tell the
      creator in plain words what the chosen one can and cannot do. Write the archetype and its reason under "Key
      decisions".
- [x] Run `npx --no -- lernapps skills --archetype <name>` with the chosen archetype. It installs the archetype's
      skills and adds the archetype's tasks to this plan.
- [x] Load skill `lernapps-explainer-design`. An explainer has the look of the runtime: write "fixed by the
      archetype" under the topic "Look and feel" of "Answers".
- [x] Interview: ask every other topic of "Answers", in order. Leave out only a topic that an answer of the creator
      already covers, and note which answer. A topic nobody answered is asked once before you write an assumption
      with "(guess)".
- [x] Load skill `lernapps-content-research` and research as it says. Write under "Notes": the strand or subject, the
      competencies by chapter with their ids, the sources you opened.
- [x] Write under "Notes" which competency goes on which page and which pages form a chapter, as "Map the content" of
      skill `lernapps-explainer-design` says. Per page, name the prerequisites the app does not practise.
- [x] Write under "Notes", one line per competency: how learners get there (they derive it, they do not only read it
      off), and which misconception the feedback catches.
- [x] Write under "Notes" the scope: what is in, what is out and why, the data range (for example "all main-group
      elements", never a silent "1–20"), the languages.
- [x] **Checkpoint:** research. Show in plain words: the strand or why none, the competencies by chapter, the didactic
      approach, the scope, every "(guess)", the sources and what is unchecked, the archetype and its reason. Stop and
      wait. Changes: change them, then ask again.
      Creator: Ja, der 4-Seiten-Schnitt passt (Orchestrator)

### Answers

<!-- The interview: per topic the creator's answer, in their words. Keep the topics. -->

- Goal: "Ich weiß, welche Form eines Pronomens ich brauche: je nachdem, ob die Person handelt, betroffen ist, etwas besitzt oder sich selbst meint." Kapitel 1 (nur dieses jetzt): Personalpronomen als Subjekt und Objekt, my, your, his, her sagen, wem etwas gehört. (Quelle: Issue lernapps/apps#471, Ersteller-Vertreter: Orchestrator.)
- Learners: Englisch, Stufe 5-6 (Kapitel 1), spätere Inkremente 7-8. Vorwissen: Hello, Millbrook! (noun, verb, adjective, sentence, tense).
- Model and focus: hello-millbrook als Muster; Schwerpunkt: Pronomen-Tabelle (Zeile je Person, Spalte je Frage), Ziehen in die richtige Spalte, Musterentdeckung.
- Hurdles: his/her richten sich nach dem Besitzer, nicht nach dem Ding (Deutsch: sein/ihr nach dem Ding); I/me, he/him verwechselt.
- Content: aus dem Issue, von mir geschrieben; Fakten aus Quellen ohne Sätze.
- Amount: Kapitel 1 mit zwei Bausteinen (Personalpronomen, Possessivbegleiter) plus Sammel-Wiederholung; Kapitel 2 später.
- Languages: deutsche Erklärtexte, englische Beispiele (britisch), Anrede du.
- Look and feel: fixed by the archetype (Look der Laufzeit); Figuren Sophie, Ellie, Peter, Amir, Mr Hill, Mrs Parker wie in hello-millbrook.
- Terms: "Ausdruck" nie "Wendung"; noun, verb, adjective, sentence, tense.
- Finding the app: Englisch Pronomen I me my, Personalpronomen, Possessivbegleiter, Klasse 5/6. (guess)

## Plan

<!--
- Map the confirmed content onto the archetype. No new content questions: a gap in the content goes back to Explore.
- The creator confirms the plan in one read. After the yes you work on your own.
-->

### Tasks

- [x] Map the content as "Map the content" of skill `lernapps-explainer-design` says, and write the result under
      "Content method".
- [x] Choose a pattern per competency as skill `lernapps-exercise-patterns` says, and add it to "Content method".
- [x] Add to "Content method" one line per page, as "Engagement" of skill `lernapps-explainer-design` says: the
      opening task, the change of activity, the reward, the story.
- [x] Add the tasks of Code, each one a piece of work that ends in a commit. First the pattern: one complete page or
      screen, `npx --no -- lernapps plan add --at pattern "<task>"`. Then the others, one call each:
      `npx --no -- lernapps plan add --at pages "<task>"`. Each task says what it builds and what it shows.
- [x] Draw a sketch of each screen, component or interactive exercise: a static SVG or image, or the steps with what
      learners see after each. Keep the files in `.vibe/sketches/`.
- [x] Show the creator, short: goal, competencies by chapter, the Code tasks, the sketches, and the content method in
      plain words (what learners see and do, what the app cannot do). At most 2 questions.
- [x] **Checkpoint:** confirm the plan and the content method. Stop and wait for an explicit yes. Changes: change
      them, then ask again.
      Creator: Ja, bestätigt; Selbsteinschätzung in die erste Version (Orchestrator)

### Content method

<!-- One line each: the patterns and where; the figures and how they are made; the data files; each component, what it
checks and what it cannot; how a later agent adds a chapter. It becomes the content guide in Code. -->
<!-- An explainer: per figure, model and component its learning action in two to four sentences
(`explainer-representation-explained`); per page its prerequisites the app does not practise, and which get a recap
page, which a link. -->

**Aufbau.** Strang-App `strand: englisch/grammatik`, `languages: [de]`, ein Kapitel `pronomen-1` („Wer? Wen? Wessen?“) mit vier Seiten. Jede Seite hat die Abschnitts-IDs `einstieg` (Sophies Szene, erste leichte Aufgabe, „Das kannst du danach“), `neu` (Tabelle wächst, Merke-Kasten), `uebung` (mind. vier, leicht → schwer), `anwenden` (`open-task` oder `speaking-task`), `weiter` (nächster Schritt der Geschichte; auf Seite 4 Rückblick). Höchstens 350 Wörter Text. Figuren: eine Szene je Seite als eigene SVG (Figuren aus `millbrook-klassenzimmer.svg` von hello-millbrook kopiert), Lizenz CC-BY-4.0, `alt` ohne Lösung; jede Szene zeigt, was die Seite erklärt (Caption sagt, worauf man achtet). Keine Datendateien, keine Vue-Komponenten: Ziehen = `matching`, Tabelle ausfüllen = `language-task` mode `table` (`prefer-built-in-block`). Audio: bf_emma, nur ganze Sätze, `regen_audio.py` aus hello-millbrook, Namen am Satzende zweisilbig (Sophie, Peter, Ellie). Terminologie: „Ausdruck“, nie „Wendung“; „Subjekt“ und „Objekt“ erst auf Seite 1 bzw. 2 in einem Satz erklärt („wer tut es“, „wen trifft es“); noun/verb gelten. Lesehilfe nur wo nötig, keine Lautschrift. Alle Übungen fragen nur Wörter ab, die vorher auf der Seite stehen; eine Tabelle, die eine Übung beantwortet, steht nicht direkt darüber; kein deutsches Wort in englischen Sätzen.

**Die wachsende Tabelle** „Klassenzimmer-Poster · Pronomen“ (je ein `table`-Block, Spalten wachsen): Seite 1 Zeilen I, you, he, she, it, we, they, Spalte „Wer tut es?“; Seite 2 + „Wen trifft es?“ (me, you, him, her, it, us, them); Seite 3 + „Wessen Ding?“ mit den Zeilen I, you, we, they (my, your, our, their); Seite 4 ergänzt he, she, it (his, her, its) und zeigt die Tabelle vollständig. Muster I – me – my.

**Muster je Kompetenz** (Fremdsprachen-Muster, leicht → schwer, Rückmeldung je Fehler in `mistakes`): personalpronomen: Zuordnen (`matching`), Form wählen (`language-task` choice mit `distractors`), Lücke (gap), Tabelle ableiten (table), Schreiben (write, Deutsch → Englisch), Diktat, Nachsprechen. possessivbegleiter: dieselbe Folge, zusätzlich Besitzer bestimmen und Satz korrigieren.

**Seiten und Engagement** (eine Zeile je Seite: Opening · Wechsel · Reward · Story):
1. `pronomen-1/wer-tut-es` (personalpronomen, Subjekt). Szene: Klassenzimmer, Ellie meldet sich. Opening: Kinder wählen, wer in „… is my friend.“ gemeint ist. Wechsel: schauen (Szene) → Tabelle lesen → Wörter in Spalte 1 sortieren. Reward: sie können Sätze mit I, you, he, she, it, we, they bauen. Story: Sophie stellt Mrs Parker die Klasse vor. Übungen: matching Person ↔ Pronomen, choice Subjekt, gap, write, true-false (it für Dinge und Tiere), Diktat. Fehler: I/me, he/she, it für Personen, you für eine und mehrere.
2. `pronomen-1/wen-trifft-es` (personalpronomen, Objekt). Szene: Peter und der Ball. Opening: „Peter sees …“ / „… sees Peter.“ – wer tut es, wen trifft es. Wechsel: Beispiele → Kinder ergänzen Spalte 2 selbst (table) → Sätze bauen. Reward: Tabelle mit zwei Spalten, sie unterscheiden Subjekt und Objekt. Story: Sophie hilft Peter beim Ballspiel. Übungen: matching I → me, choice Subjekt oder Objekt im Satz, gap, ordering, write, Diktat. Fehler: „Me like“, „I like he“, he/him, we/us.
3. `pronomen-1/my-your` (possessivbegleiter: my, your, our, their). Szene: Taschen und Jacken im Flur. Opening: „Whose bag is this?“ – Kinder wählen. Wechsel: Szene → Muster I – me – my selbst entdecken (table) → Besitzer wählen. Reward: Spalte 3 für I, you, we, they. Story: Sophie sortiert Taschen für Mrs Parker. Übungen: choice, gap, matching Besitzer ↔ Wort, write, Diktat. Fehler: me bag, I bag, you/your.
4. `pronomen-1/his-her` (possessivbegleiter: his, her, its + Schlussübung). Szene: Ellie (rote Jacke) und Peter (gelbe Jacke) mit Dingen. Opening: Wessen Ding? Kinder wählen his oder her. Wechsel: Bild zum Unterschied zum Deutschen (her brother = Besitzerin Ellie, his sister = Besitzer Peter) → Besitzer bestimmen → Korrigieren. Reward: vollständige Tabelle; Rückblick. Story: Mrs Parker liest die Namen auf den Sachen vor; Ausblick auf später. Übungen: matching Besitzer ↔ Wort, choice (Besitzer bestimmt), gap, Korrigieren (write mit Fehlersatz), Schlussübung über die ganze Tabelle, Diktat, `open-task`. Fehler: his/her nach dem Ding, its/it's, he/his.

**Spätere Ergänzung (Kapitel 2):** Kapitel `pronomen-2` (mine/yours, myself, each other, Stufe 7-8) erweitert dieselbe Tabelle um zwei Spalten. Selbsteinschätzung: in Commit, je Seite zwei Übungen.


## Code

<!--
- Build the app, locally on `work`, on your own. After each task: `plan done`, then one commit with the work and this
  plan. The hooks check each commit; a failing check is fixed from its message, as skill `lernapps-cli` says.
- What you cannot decide: choose, write it under "Key decisions" with "(guess)", go on.
- The creator asks for a change: say your reading in one sentence first, then change every place it holds for
  (`feedback-applied-everywhere`).
-->

### Tasks

- [x] Load skill `lernapps-cli`. Create the app as its section "Create" says:
      `npx --no -- lernapps create --archetype explainer`.
- [x] Fill the content guide `.agents/skills/app-content/SKILL.md` from "Notes" and "Content method": every heading,
      no "FILL IN" left. Commit it before any content.
- [x] Load skill `lernapps-explainer`.
- [x] Load skill `lernapps-content-questions`. Read whole, with your file tool:
      `.agents/skills/lernapps-explainer/references/blocks.md` and
      `.agents/skills/lernapps-explainer/references/exercises.md`. A foreign language: also
      `references/language-tasks.md` in the same folder. A component in the plan: also `references/components.md`.
- [x] Decide whether the app needs `scope`, as "`scope`" in
      `.agents/skills/lernapps-explainer/references/structure.md` says. Write the choice under "Key decisions".
- [x] Page 1 pronomen-1/wer-tut-es complete: scene SVG, table column 1, at least four exercises easy to hard with mistakes, dictation audio with bf_emma, speaking task; checks on
<!-- tasks: pattern (1 added): the one page or screen that is the pattern for the others -->
- [ ] **Checkpoint:** the pattern page. Load skill `lernapps-learner-check` and do its learner check on the page. Fix
      what it finds. Then show the creator the page and ask whether the others may follow it. Stop and wait. A
      change: change the pattern first.
- [ ] Page 2 pronomen-1/wen-trifft-es: scene, table column 2 derived by learners, exercises, audio
- [ ] Page 3 pronomen-1/my-your: scene, table column 3, pattern I - me - my, exercises, audio
- [ ] Page 4 pronomen-1/his-her: scene, his/her follows the owner, full table, final exercise, open task, look back, audio
- [ ] app.yaml, chapter.yaml, selfAssessment, Sources in content guide, language and sound check by sub-agent
<!-- tasks: pages (4 added): the other pages or screens, after the pattern -->
- [ ] Update the content guide so that it describes the app as built (`app-content-matches`).
- [ ] Run `npx --no -- lernapps check` until it passes.
- [ ] Look at every screen and state, at 360 px and on a desktop, as "Look at the app" of skill `lernapps-cli` says.
      Compare each with its sketch.
- [ ] Do the whole-app check of skill `lernapps-learner-check`. Fix what it finds and write under "Notes" what you
      fixed.

## Commit

<!--
- Put the app on GitHub, publish it with the creator's yes, then list it. A push to `main` publishes.
- Open the pull requests (to `main`, to the catalog) without asking: they publish nothing.
- The creator asked to stop before publishing (a trial): stop here and say so.
-->

### Tasks

- [ ] Load skill `lernapps-explainer-self-assessment`. Add the self-assessment as it says, or write under "Key
      decisions" why the app has none. Commit.
- [ ] Load skill `lernapps-github`. Set up the repository and Pages as it says. Ask for the repository's name and
      every click only the creator can make, in one message.
- [ ] Push `work`, open the preview pull request and see its checks to green, as skill `lernapps-github` says.
- [ ] **Checkpoint:** publish. Show what the app does and the preview link from the comment "Vorschau der App". Ask
      whether it may go online. Stop and wait for the yes.
- [ ] Load skill `lernapps-commit`. Publish as skill `lernapps-github` says: `work` into `main` as one squash commit,
      the run of `Pages` watched to its end.
- [ ] Open the address the job `deploy` printed and confirm that the app shows. Never use a derived address.
- [ ] Load skill `lernapps-listing`. Write the entry under "Entry draft" as it says, with the creator's answer to
      "Finding the app".
- [ ] Fill the retrospective.
- [ ] Commit this plan on `main` and push it: the listing check and the review read it there.
- [ ] **Checkpoint:** list. Open the listing pull request as skill `lernapps-listing` says, without asking first: the
      pull request is the review. See it to "bestanden", then show the creator the pull request and its result.
- [ ] If the plan changed since its last push, commit it on `main` and push again.

### Entry draft

<!-- YAML valid against the entry schema the listing skill names. Only known values, never invented. -->

```yaml
```

## Retrospective

<!-- At the end of Commit, before the listing pull request. Facts, short, no names. Read by review and evals. -->

### Phases reached

<!-- Last phase completed, checkpoints passed. E.g. "commit; confirmed, published". -->

### Creator turns after the plan

<!-- Number of creator messages after the confirmation, topic of each. Target: at most 3. -->

### Where I had to guess

<!-- Each gap in plan, skills, messages or answers, and your choice. "None" if none. -->
