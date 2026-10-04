# The Ed Answer Key — CF3.4.2 Contact Alias

Branch: `51.3.11-CF3.4.2-contact-alias`

This patch builds on CF3.4.1 and changes only the public footer contact identity.

## Footer contact

Displayed address: **EdAnswerKey@sagegap.com**  
Mail target: `mailto:edanswerkey@sagegap.com`

The mixed-case display is for readability and branding. Email routing remains case-insensitive in normal mail systems.

## Preserved behavior

- Header and footer navigation behavior remains unchanged.
- Footer SageGap link still opens in a new tab.
- Apple-native Conversation Finder player remains unchanged.
- Seven Finder areas, 21 guided choices, and recommendation clusters remain unchanged.

## Before publishing

Create or verify the `edanswerkey@sagegap.com` alias with the email provider that hosts `sagegap.com`, route it to the intended mailbox, then test inbound mail and reply behavior. See `docs/EMAIL-ALIAS-SETUP.md`.
