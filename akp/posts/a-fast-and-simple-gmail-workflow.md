title: A Fast and Simple Gmail Workflow
description: How I learned to stop worrying and tame my inbox
date: 2022-01-07

I created my main Gmail account in September 2004, and since then I've made
almost 55,000 threads. That's about ten threads a day for 17 years. At times
I've managed to keep that under control. But email becomes secondary in the
high tides of life, and ten threads a day soon becomes a storm of hundreds.

Sometimes I've declared [email bankruptcy][bankruptcy], but it feels like a
failure each time I do so. What opportunities have I missed because I didn't
follow up in time? And how can I expect others to reply to me if I don't do the
same for them?

[bankruptcy]: https://en.wikipedia.org/wiki/Email_bankruptcy

So I've started using a simple workflow to manage my inbox, no matter how large
it might get:

1. Start with the oldest email I have.
2. If I can handle it quickly, do so. Otherwise, deal with it later.
3. Move to the next one.

It's simple, but the trick is in the details. With the right shortcuts and the
right labels, I can handle hundreds of emails in one go. Email backlogs are no
longer intimidating, and I can keep my inboxes clear.


# The setup

I use the default Gmail view and the default sort order. So my inbox is a
simple list with the newest emails first.

The critical extension is *Keyboard shortcuts* under *Settings > General*. You
can type `?` at any time to see all of the available shortcuts, but four are
enough for this workflow to work:

- `}` -- archive and move to the next newest
- `r` -- reply
- `l` -- add a label
- `⌘+Enter` -- send


# The core workflow

First I open the oldest email I have. If my inbox is truly massive, I [sort by
oldest first][sort] so I don't have to go looking for it.

[sort]: https://gsuitetips.com/tips/gmail/sort-email-by-oldest-first/

The email is open with no distractions to pull me away. Then I decide what kind
of email I'm looking at:

- **Irrelevant** -- Spam, irrelevant mailing lists, and emails that just aren't
  worth the time. For most mailing lists, Gmail has an *Unsubscribe* link next
  to the sender's email address. Otherwise, hit `}` to move on.

- **No reply** -- For announcements or emails that are outdated. Hit `}` to
  move on.

- **Fast reply** -- For emails I can write within a minute or so. `r` to reply
  and `⌘+Enter` to send. Then hit `}` to move on.

- **Slow reply** -- If I need more time to reply, I add a special label to the
  email so I can find and follow up on it later. I type `l` to pull up the
  label menu, enter my label name, hit `Enter`, then hit `}` to move on.

    I use a short label name like `!` since it's faster to type. So the full
    sequence is something like `l!<enter>}`.


The main friction here is clicking the *Unsubscribe* link. Otherwise, I can get
through the first three types here in seconds.


# Extending the workflow

If this basic workflow works for you, here are some simple ways to extend it:

- **Undo** -- Use `z` to undo an action. For example, maybe you didn't mean to
  archive the email you were looking at.

- **Spam and trash** -- Use `!` to mark emails as spam and `#` to send emails
  to the trash. Unfortunately this returns you to the main inbox, so I don't
  really like using it. So I usually just hit `}` to archive everything.

And if I decide this workflow needs changing, I'll post an update.
