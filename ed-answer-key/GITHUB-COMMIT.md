# GitHub Commit Handoff

Suggested branch:

```text
ed-answer-key/cf3.1-release-candidate
```

Suggested commit message:

```text
feat(ed-answer-key): integrate production Conversation Finder archive

- expand Finder to 55 substantive conversations
- add 7 listener-centered areas and 21 guided questions
- add Start Here and Also Worth Hearing recommendation clusters
- centralize runtime content in conversations.json
- preserve independent Finder and player state
- use canonical RSS audio playback
- fix player replay state after close
- add Episode 57+ publishing workflow and validation tooling
```

If this is replacing an existing `/ed-answer-key/` directory, copy the contents of this folder into that directory, review the diff, run the validator, commit to the release-candidate branch, deploy, and complete the final hosted-browser regression pass before promoting the branch to the production baseline.
