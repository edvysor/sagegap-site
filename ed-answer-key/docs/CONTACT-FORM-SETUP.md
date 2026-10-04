# Ed Answer Key Contact Form — Production Verification

Dedicated Formspree endpoint:
`https://formspree.io/f/xkjowkav`

Dedicated form:
**Ed Answer Key Contact**

Notification destination:
**david@sagegap.com**

## Gmail filter

From:
`noreply@formspree.io`

Has the words:
`"Ed Answer Key Contact"`

Action:
Apply the red **Ed Answer Key** label.

## Live verification after deployment

1. Open the live Ed Answer Key site.
2. Click **EdAnswerKey@sagegap.com** in the footer.
3. Submit:
   - Name: Website QA
   - Email: an outside address you control
   - Topic: General inquiry
   - Message: CF3.4.4 production contact test
4. Confirm the site displays **Message sent.**
5. In Formspree, open **Ed Answer Key Contact → Submissions** and confirm the entry appears.
6. Confirm the Formspree notification reaches `david@sagegap.com`.
7. Confirm Gmail applies the red **Ed Answer Key** label.
8. Reply and confirm the From identity is **The Ed Answer Key <edanswerkey@sagegap.com>**.

If the site reports an error, open the browser developer console. CF3.4.4 logs Formspree's response status/provider payload for diagnosis while keeping the listener-facing message simple.
