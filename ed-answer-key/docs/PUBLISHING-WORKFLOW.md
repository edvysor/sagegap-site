# The Ed Answer Key — Episode 57+ Publishing Workflow

This is the operational maintenance path for Conversation Finder after CF3.1. The rule is simple: **publish first to the canonical Libsyn feed, then update the editorial data layer; do not hand-edit recommendation logic in the HTML.**

## 1. Canonical intake
1. Publish the episode in Libsyn and confirm it appears in `https://feeds.libsyn.com/494513/rss`.
2. Capture publisher-controlled metadata: title, publication date, GUID, Libsyn item ID, season, episode number, episode type, duration, RSS enclosure audio URL, description/content, and image metadata if present.
3. Assign the internal catalog ID using the existing convention: `TEAK-S##E##` (or the appropriate nonstandard suffix for a trailer/special item).
4. Do not overwrite the publisher GUID or Libsyn item ID with the internal catalog ID.

**Gate A:** the new RSS item must parse cleanly, have a unique GUID and Libsyn item ID, and have an audio enclosure URL before it proceeds.

## 2. Content enrichment
Using the publisher description/content as the initial evidence basis, add:
- central issue
- concise source-grounded summary
- audience signals
- series / arc
- content mode
- up to three useful takeaways
- evidence scope / confidence

If the RSS description does not support a necessary editorial judgment, review the transcript/audio and explicitly change the evidence scope. Do not silently infer unsupported detail.

**Gate B:** enrichment must describe the episode without assigning a recommendation yet.

## 3. Taxonomy placement
Evaluate the episode against the seven current top-level areas:
- Family & School
- Learning & Classroom
- Student Support & Well-Being
- Teaching & Educator Life
- Assessment & Accountability
- School Systems & Leadership
- Community, Identity & Belonging

Assign one primary area and up to two legitimate secondary areas. Add cross-cutting facets such as AI & Technology, Multilingual Learning, IEP/504, School Choice, Discipline & Safety, or other established facets as appropriate.

Do **not** create a new visible top-level area because of one new episode. Revisit taxonomy only when a meaningful archive cluster has accumulated.

**Gate C:** exactly one primary area; secondary areas only where the listener could reasonably enter through that path.

## 4. Editorial role
Within every eligible area, assign one role:
- **Anchor** — broad, evergreen entry point
- **Situational** — best for a specific circumstance
- **Supporting** — useful companion perspective
- **Context / Story** — lived experience, history, identity, or reflection

Roles are area-specific. An episode may be Anchor in its primary area and Supporting in a secondary area.

## 5. Listener-question mapping
Map the episode to every existing visible question it genuinely answers. The current UX is intentionally fixed at three questions per area. Do not add a fourth visible question simply because a new episode has a narrow subject.

If the episode exposes a listener need that none of the current 21 questions can honestly contain, log it as a **question-library review candidate**. Accumulate evidence before changing Step 2 of the Finder.

## 6. Recommendation-cluster review
For every question the new episode maps to, compare it with the existing cluster using this order:
1. question fidelity
2. editorial function
3. breadth/accessibility
4. complementarity with the other recommended conversations
5. avoidance of redundancy

Chronology is **not** a ranking factor. A new episode does not automatically become Start Here.

Possible outcomes:
- no change to the visible cluster
- replace/add an `Also worth hearing` conversation
- become the new `Start Here` because it answers the question more directly

Each question must still resolve to **one Start Here + 2–3 Also worth hearing** conversations.

## 7. Regenerate `conversations.json`
Update the structured production data only. The HTML should continue to read:
- areas
- questions
- episode metadata
- Start Here IDs
- Also worth hearing IDs
- RSS enclosure audio URLs

Keep Finder state and player state independent. Navigation must never change playback. Only `Listen Now` may change the player.

## 8. Run validation and regression QA
Run:

```bash
python validate-conversations.py conversations.json
```

Then run the browser regression suite. Release only when all checks pass, including:
- 7 visible areas
- 3 visible questions per area
- correct Start Here title for all 21 questions
- 2–3 companion recommendations per question
- related-card promotion changes the primary recommendation without changing playback
- changing topics/questions does not interrupt or replace current playback
- closing and replaying the same episode restores the correct audio source
- disclosure `+ / −` behavior is truthful
- desktop and mobile layouts have no unintended horizontal overflow
- embedded fallback and external `conversations.json` contain the same production structure

## 9. Release naming
Increment the Finder data/integration branch without changing the canonical site identity. Suggested pattern:

`51.3.11-CF3.x-<short-purpose>`

Record the data and HTML SHA-256 hashes in the release manifest. Keep the previous validated package as rollback.

## 10. Periodic architecture review
Do not reconsider the seven-area taxonomy on every episode. Review the information architecture after a meaningful batch (recommended: approximately 8–12 new substantive conversations) or when repeated question-library review candidates reveal a genuine new listener need.
