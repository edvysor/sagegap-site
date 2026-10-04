# The Ed Answer Key — CF3.4.1 Layout Fix

This is the commit-ready correction to CF3.4 Guided Navigation & Mobile Copy.

## Fixed
The legacy Finder stylesheet applied its circular step-number styling to every `span` inside a stage label. CF3.4 introduced a `span.finder-stage-copy` wrapper, so the text wrapper inherited a 28×28 badge box and its text overflowed/overlapped.

CF3.4.1 scopes those legacy rules to `.finder-stage-number` and adds a defensive reset to the copy wrapper.

## Preserved
- 7 Conversation Finder areas
- 21 shortened listener choices with descriptors
- 55 Finder-eligible conversations
- Apple Podcasts native episode player
- Finder/player-state independence
- Footer-only SageGap new-tab behavior
- Existing recommendation clusters
