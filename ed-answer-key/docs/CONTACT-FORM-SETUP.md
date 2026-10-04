# Ed Answer Key Website Contact Form — CF3.4.3

## Runtime behavior
The footer continues to display `EdAnswerKey@sagegap.com`. With JavaScript enabled, clicking it opens the branded on-site contact dialog. If JavaScript fails, the original `mailto:` fallback still opens the visitor's mail application.

## Delivery
The form posts to the existing, proven SageGap Formspree endpoint:

`https://formspree.io/f/xdabadpk`

The current Formspree destination is `david@sagegap.com`, so website submissions reach the same Google Workspace inbox without creating another paid mailbox. Each Ed Answer Key submission carries:

- `form_type = Ed Answer Key Contact`
- `_subject = Ed Answer Key Website Contact`
- `source = Ed Answer Key website footer`
- the visitor's name, email, selected topic, message, and page URL

## Gmail visual labeling
Because Formspree sends the notification to `david@sagegap.com` rather than directly to the alias, the existing Gmail filter `to:edanswerkey@sagegap.com` will not label these website-form notifications. Add a second filter for website submissions:

`from:noreply@formspree.io "Ed Answer Key Contact"`

Apply the **Ed Answer Key** label and keep the message in the Inbox. This preserves the red visual channel for both direct alias mail and website-form mail.

## Reply identity
A Formspree notification is addressed to `david@sagegap.com`, so Gmail may default the reply's From address to David. Before sending a reply to a website submission, choose **The Ed Answer Key <edanswerkey@sagegap.com>** from Gmail's From selector.

For fully automatic alias-aware replies in the future, create a dedicated Formspree form whose destination is `edanswerkey@sagegap.com`, then replace the action URL in `index.html`. The current build works immediately using the existing endpoint.

## Verification
1. Deploy the build to GitHub.
2. Click `EdAnswerKey@sagegap.com` in the footer.
3. Submit a test message.
4. Confirm the success state appears without leaving the page.
5. Confirm a Formspree notification arrives at `david@sagegap.com`.
6. Confirm the Gmail Ed Answer Key label is applied after the filter above is created.
7. Reply using the Ed Answer Key From identity.
