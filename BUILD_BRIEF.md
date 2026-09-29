# Ed Answer Key Hero Build Brief v27

## Objective
Rebuild the right-side Ed Answer Key hero so its visible default state matches the approved target artwork with high fidelity while preserving live interaction for the three metric cards.

## Non-negotiable visual reference
The approved target image is the visual source of truth for the hero. Do not approximate its headline typography, line weight, spacing, signal field, glow, or badge with substitute CSS when the exact approved artwork can be retained.

## Architecture
1. Use the approved target artwork as the upper and middle visual layer of the hero.
2. Crop the artwork to the black rounded card only.
3. Remove the baked-in 50+ Episodes, 3 Audiences, and 1 Mission boxes from the raster artwork.
4. Preserve the approved A SageGap Podcast badge, THE PODCAST HOME FOR kicker, The Ed / Answer / Key title stack, red signal field, rings, waveform, and their exact placement from the target artwork.
5. Overlay three live HTML metric cards into the cleared lower black region.
6. Embed the processed hero artwork directly in the HTML as a data URI so the page does not depend on a separate hero image file.

## Visual fidelity requirements
- Card proportion must follow the approved target portrait ratio.
- Exterior card corners must remain deeply rounded.
- Background must remain near-black with the same soft tonal falloff as the approved target.
- Headline contrast must be preserved exactly from the target: bright white for The Ed and Key, saturated red for Answer.
- The title must retain the exact three-line stack shown in the reference.
- The red signal field must remain on the right and must not move into the title zone.
- The waveform must remain crisp inside the softer red field.
- The upper badge and kicker must retain the approved scale and relative placement.
- Do not add a white frame or secondary border around the artwork.

## Interactive metric cards
Default state should visually match the target static cards:
- three equal cards in a single row
- dark translucent glass surface
- thin soft gray border
- rounded corners
- large white number
- muted uppercase label
- no extra explanatory copy visible by default

Hover, focus, and tap behavior:
- lift 4 to 5 pixels maximum
- scale no more than 1.015
- border shifts subtly toward red
- a restrained internal red glow appears
- number and label remain fully readable
- supporting copy fades into the lower part of the same card
- motion should feel premium and controlled, not playful
- card stays fully inside the hero boundary
- only one tapped card is active at a time
- Escape clears an active card
- reduced-motion preferences must be respected

Supporting copy:
- 50+ Episodes: Short conversations for real school questions.
- 3 Audiences: Families, educators, and school leaders.
- 1 Mission: Clarity that supports the next step.

## Responsive behavior
- Desktop: preserve the target portrait composition and exact visual hierarchy.
- Tablet: center the hero card below the left hero copy while preserving its aspect ratio.
- Mobile: keep all three metrics in one row so the poster composition remains recognizable. Reduce type inside the metric cards rather than stacking them vertically.
- Do not crop the approved title or signal field at any breakpoint.

## Accessibility
- The decorative raster artwork is aria-hidden.
- The hero card has a descriptive accessible label.
- Metric cards are keyboard focusable.
- Enter and Space toggle a metric card on touch/keyboard layouts.
- Escape closes the active state.
- Respect prefers-reduced-motion.

## Copy and implementation constraints
- Do not use em dash characters in site copy.
- Preserve the current SageGap to Ed Answer Key brand hierarchy.
- Do not modify unrelated page sections in this pass.
