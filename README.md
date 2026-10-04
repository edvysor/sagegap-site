# The Ed Answer Key — CF3.4.4 Dedicated Contact Endpoint

This release keeps the Conversation Finder, Apple-native listening experience, guided mobile navigation,
footer SageGap new-tab behavior, and Ed Answer Key email identity intact.

## Contact reliability change

The footer contact form now posts to the dedicated Formspree form:

`https://formspree.io/f/xkjowkav`

Form name: **Ed Answer Key Contact**

Operational notification inbox: **david@sagegap.com**

Public reply identity: **The Ed Answer Key <edanswerkey@sagegap.com>**

## Reliability refinements

- Dedicated Ed Answer Key Formspree endpoint; no longer shares the Teacher Copilot endpoint.
- Removed the custom `_gotcha` honeypot so there is no silent-discard path from that field.
- Uses Formspree's current `subject` field.
- Keeps `form_type=Ed Answer Key Contact` for Gmail filtering.
- Shows success only after a successful Formspree HTTP response.
- Logs Formspree HTTP/provider details to the browser console if submission fails.
- Keeps a visible `mailto:edanswerkey@sagegap.com` fallback.

## Gmail filter

From:
`noreply@formspree.io`

Has the words:
`"Ed Answer Key Contact"`

Apply label:
**Ed Answer Key**

Do not skip the inbox.
