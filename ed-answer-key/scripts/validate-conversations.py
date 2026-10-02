#!/usr/bin/env python3
from pathlib import Path
import json, sys

path = Path(sys.argv[1] if len(sys.argv) > 1 else 'conversations.json')
data = json.loads(path.read_text(encoding='utf-8'))
errors = []
areas = data.get('areas', [])
questions = data.get('questions', {})
episodes = data.get('episodes', {})

if len(areas) != 7: errors.append(f'expected 7 areas, found {len(areas)}')
if len(questions) != 21: errors.append(f'expected 21 questions, found {len(questions)}')
if sum(1 for e in episodes.values() if e.get('finderEligible')) != 55:
    errors.append('expected 55 Finder-eligible episodes')

for area in areas:
    qids = area.get('questionIds', [])
    if len(qids) != 3: errors.append(f"{area.get('id')}: expected 3 questions")
    for qid in qids:
        if qid not in questions: errors.append(f'{area.get("id")}: missing question {qid}')

for qid, q in questions.items():
    sid = q.get('startHere')
    also = q.get('alsoWorthHearing', [])
    if sid not in episodes: errors.append(f'{qid}: invalid Start Here {sid}')
    if not (2 <= len(also) <= 3): errors.append(f'{qid}: expected 2–3 companions')
    if sid in also: errors.append(f'{qid}: Start Here repeated among companions')
    if len(also) != len(set(also)): errors.append(f'{qid}: duplicate companions')
    for cid in also:
        if cid not in episodes: errors.append(f'{qid}: invalid companion {cid}')

for cid, ep in episodes.items():
    if ep.get('finderEligible') and not ep.get('audioUrl'):
        errors.append(f'{cid}: missing audioUrl')

if errors:
    print('FAIL')
    for e in errors: print('-', e)
    sys.exit(1)
print('PASS')
print(f"areas={len(areas)} questions={len(questions)} finderEligible={sum(1 for e in episodes.values() if e.get('finderEligible'))}")
