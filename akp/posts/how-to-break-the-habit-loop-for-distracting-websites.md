title: How to Break the Habit Loop for Distracting Websites
description: The simple changes you can make to reclaim your attention 
date: 2022-01-11
order: 3

The basic structure of a habit is *cue &rarr; craving &rarr; response &rarr;
reward*:

1. The <dfn>cue</dfn> is the context that triggers the habit, such as feeling
   bored or anxious.

2. The <dfn>craving</dfn> is the feeling that you should take some action, such
   as reaching for your phone and opening up YouTube.

3. The <dfn>response</dfn> is the action, such as watching a video.

4. The <dfn>reward</dfn> is the result that reinforces the habit, such as the
   dopamine hit of novel content.

Weaken these four and the habit eventually fades. For example, if your phone
is harder to reach, it'll be more difficult to act on the habit.

But since this is ostensibly a tech blog, here are some tech things you can do
with the same effect:


# Edit `/etc/hosts`

Your [`/etc/hosts`][hosts] file defines redirects for different websites.
Redirecting a website to `localhost` (IP address `127.0.0.1`), as is done here,
has the effect of preventing you from visiting that website:

    #!text
    127.0.0.1  twitter.com
    127.0.0.1  www.twitter.com
    127.0.0.1  reddit.com
    127.0.0.1  www.reddit.com
    127.0.0.1  youtube.com
    127.0.0.1  www.youtube.com
    127.0.0.1  tumblr.com
    127.0.0.1  www.tumblr.com
    127.0.0.1  twitch.tv
    127.0.0.1  www.twitch.tv

Yes, `www` [is necessary][www] if the site uses it.

[hosts]: https://tldp.org/LDP/solrhe/Securing-Optimizing-Linux-RH-Edition-v1.3/chap9sec95.html
[www]: https://unix.stackexchange.com/questions/439120/why-do-i-need-www-and-non-www-in-etc-hosts

If these changes don't take effect, run:

    #!sh
    # macOS only
    dscacheutil -flushcache

to flush the cache.


# [iOS] Enable *Content & Privacy Restrictions*

If you have an iOS device, you can also enable per-website restrictions:

1. Go to *Content & Privacy Restrictions* in *Settings*.
2. Go to *Content Restrictions &rarr; Web Content*.
3. Select *Limit Adult Websites* (sketchy name, I know).
4. Add whatever websites you want to block to the *Never Allow* list.


# Does this work?

These changes are just speed bumps I use to remind myself that I probably
*don't* want to be using this website. If I have a real need, I can easily
circumvent these changes and use them when I need to.

If your problem is more serious, I've heard good things about
[Freedom](https://freedom.to/), but I think someone could circumvent basically
*any* content blocker if they were determined enough.

!!! endnotes
    This post was written in ... 18 minutes?! Wow, I need to learn to be faster.
