# Changelog

## CF3.4.3 — Website Contact Form
- Converts the footer Ed Answer Key email interaction into a real on-site contact form.
- Reuses the existing SageGap Formspree endpoint already delivering to `david@sagegap.com`.
- Adds source/form-type metadata so Ed Answer Key submissions can be filtered separately in Gmail.
- Keeps `EdAnswerKey@sagegap.com` visible and preserves a `mailto:` fallback.
- Adds success, loading, error, outside-click, Escape-key, and mobile dialog states.
- Preserves CF3.4.1 guided navigation, Apple-native player behavior, recommendation data, and footer SageGap new-tab behavior.

# Changelog

## 51.3.11-CF3.4.2-contact-alias

- Replaced the Ed Answer Key footer contact `hello@sagegap.com` with `EdAnswerKey@sagegap.com`.
- The live link uses `mailto:edanswerkey@sagegap.com`.
- No header, Finder, player, taxonomy, recommendation, or SageGap-link behavior changed.


## 51.3.11-CF3.4.1-layout-fix

### Layout correction
- Corrected the overlapping Conversation Finder step headings introduced in CF3.4.
- Restricted legacy circular step-badge styling to `.finder-stage-number` only.
- Added defensive resets so the title/helper-copy wrapper cannot inherit badge dimensions, background, radius, or shadow.
- Preserved the shortened topic/question copy, guided three-step navigation, Apple-native player, recommendation graph, and footer SageGap new-tab behavior.

## 51.3.11-CF3.4-guided-mobile-nav
- Introduced short intent labels + descriptors and explicit three-step navigation.
