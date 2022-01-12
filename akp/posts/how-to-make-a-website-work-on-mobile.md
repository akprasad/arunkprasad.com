title: How to Make a Website Work on Mobile
date: 2022-01-06
description: The specific HTML and CSS you need to make sites mobile-friendly,
             and the tools to test your site across multiple devices.

Ask Google [how to make a website work on mobile][q] and you can't help but
weep at the results. "Use frameworks" and "avoid pop-ups" is fine advice, but
it's hardly useful to a technical user in the trenches.

In this post I'll describe the specific things I do to make websites
mobile-friendly, including some of the gotchas I've hit in the past.

[q]: https://www.google.com/search?q=how+to+make+a+website+work+on+mobile


# The essential setup

Stick this in your page `<head>`:

    #!html
    <meta name="viewport" content="width=device-width, initial-scale=1">

And add this to your CSS:

    #!css
    html {
      -webkit-text-size-adjust: 100%;
      text-size-adjust: 100%;
    }

The [viewport meta tag][viewport] is vital:

- When it's missing, the browser will render in desktop mode, and all of your
  responsive CSS rules will be ignored.

- When it's present, the browser will properly resize your website to the
  device, and all of your responsive CSS rules can take effect.

[`text-size-adjust`][tsa] controls the browser's text rendering behavior:

- By default, the browser might apply a text resizing algorithm to make the
  page readable on mobile. But if you're using your own responsive CSS, this
  algorithm is unpredictable and can create weird bugs.

- By setting this to `100%`, the browser renders text predictably, which means
  that your text will always look as you expect it to.

Older versions of Safari support only `-webkit-text-size-adjust`, so we should
include both.

!!! note
	This [Stack Overflow answer][so] has some useful discussion on
	`text-size-adjust` and how to use it safely.

[viewport]: https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag
[android]: https://developer.android.com/guide/webapps/targeting
[tsa]: https://developer.mozilla.org/en-US/docs/Web/CSS/text-size-adjust
[so]: https://stackoverflow.com/a/3428477


# Responsive CSS

The basic structure of this is simple:

    #!css
    @media screen and (min-width: 640px) {
      /* Your CSS */
    }

    @media screen and (min-width: 1280px) {
      /* Your CSS */
    }


For the specific screen sizes, I just refer to a framework like
[Tailwind][tw-breakpoints].

[tw-breakpoints]: https://tailwindcss.com/docs/responsive-design


# Debugging

I'm less familiar with Safari, but [Firefox][ff-dev] and [Chrome][chrome-dev]
both have excellent developer consoles that let you emulate specific device
sizes.

For more thorough testing, I love Browserstack's [Responsive Design
Testing][bs] tool, which shows you how your site renders on about a dozen
different devices. I've only ever used the free tier.

[ff-dev]: https://developer.mozilla.org/en-US/docs/Tools/Responsive_Design_Mode
[chrome-dev]: https://developer.chrome.com/docs/devtools/device-mode/
[bs]: https://www.browserstack.com/responsive


# If you really need a framework

In yet another win for [composition over inheritance][coi], the last few years
have seen the rise of compositional CSS frameworks like [Tachyons][tachyons]
and [Tailwind][tailwind]. Adam Wathan (one of the Tailwind devs)
[explains][adam] the philosophy of this approach better than I could.

I don't know where the industry will move a few years from now, but for now, I
love both of these frameworks and highly recommend them.


[coi]: https://en.wikipedia.org/wiki/Composition_over_inheritance
[tachyons]: http://tachyons.io/
[tailwind]: https://tailwindcss.com/
[adam]: https://adamwathan.me/css-utility-classes-and-separation-of-concerns/
