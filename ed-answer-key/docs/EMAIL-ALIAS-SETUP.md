# Ed Answer Key email alias setup

Public display: **EdAnswerKey@sagegap.com**  
Canonical mailbox alias: `edanswerkey@sagegap.com`

## Sequence

1. **Create the alias with the mail provider for `sagegap.com`.** Add `edanswerkey@sagegap.com` as an alias, group, forwarder, or routed address attached to the mailbox that should receive Ed Answer Key inquiries.
2. **Verify inbound delivery.** From an unrelated email account, send a message to `edanswerkey@sagegap.com` and confirm it arrives in the intended mailbox without being quarantined or rejected.
3. **Decide reply identity.** If replies should visibly come from `EdAnswerKey@sagegap.com`, configure the provider's “send as”/alias identity and complete any verification it requires. If not, replies may continue to come from the underlying mailbox.
4. **Test reply and threading.** Reply to the external test message and confirm the From address, reply-to behavior, threading, and spam handling are what you want.
5. **Publish the website patch.** Commit CF3.4.2 after mail delivery works. The footer link is `mailto:edanswerkey@sagegap.com` while the visible text is `EdAnswerKey@sagegap.com`.
6. **Test from the live Ed Answer Key site.** Click the footer contact on desktop and mobile, confirm the mail composer opens to the correct recipient, send a final live test, and verify receipt.
7. **Keep `hello@sagegap.com` for SageGap.** The parent SageGap site can continue using its general-purpose contact, while Ed Answer Key has a clearly branded contact channel.

## Important

Publishing the `mailto:` link does not itself create a mailbox. The alias must exist with the email provider first for messages to be deliverable.
