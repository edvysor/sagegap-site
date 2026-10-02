# The Ed Answer Key — CF3.3 Apple-native Conversation Finder Player

Branch: `51.3.11-CF3.3-apple-native-player`

## What changed
The Conversation Finder now uses the same Apple Podcasts embedded-player surface as the Signature Listening Room. The Ed Answer Key retains the listening-room shell, typography, metadata, spacing, close behavior, and Finder logic; Apple supplies the live episode artwork and playback interface.

### Episode resolution
The RSS catalog remains canonical. On `Listen Now`, the static GitHub site resolves the selected conversation to Apple Podcasts in this order:
1. Known cached Apple episode ID when available.
2. Apple show lookup matched by the RSS GUID / Apple `episodeGuid`.
3. Normalized episode-title match.
4. Per-episode Apple Search API fallback.

The lookup uses JSONP so it works from a static GitHub Pages deployment without a backend or CORS dependency. Resolved IDs are cached for the browser session.

## Behavior retained
- 7 top-level Finder areas and 21 guided questions.
- 55 Finder-eligible conversations.
- One Start Here + 2–3 Also worth hearing recommendations per question.
- Finder state stays independent from listening state. Changing topics/questions/recommendations does not replace an open player.
- The player changes only after an explicit `Listen Now`.
- Opening the Signature Listening Room closes the Finder player, and vice versa.

## Rendering note
Apple may block or partially render its iframe inside sandboxed preview environments. The authoritative visual test is the GitHub/Cloudflare-hosted page, where the Signature Listening Room already demonstrates the same embed pattern successfully.
