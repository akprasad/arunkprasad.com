title: What are Fundamentals?
description: In which I figure out what I mean by "fundamentals"
date: 2022-01-11

I'm still thinking about the amateur/professional distinction I [wrote about
recently][ap], not least because I blundered into it.

Before that post, I had been planning to write about a minor productivity hack.
But the more I followed that line, the more I felt uneasy. Then suddenly, an
idea I had heard about all my life finally clicked into place, and I felt my
perspective completely change.

[ap]: /log/amateurs-and-professionals/

As a reminder, "amateur" and "professional" are *attitudes*. And the
professional attitude is to master and treasure the fundamentals.

The writing on fundamentals that I'm familiar with is vigorous and inspiring.
But I also often find that it's either so abstract that I don't know what to
actually *do* or so localized that I can't use it for my work.

In this post, I'm doing some ground clearing for myself so that I better
understand what fundamentals are.


## Fundamentals in the games of life

<dfn>Game theory</dfn> is a formal way of studying how people act and how they
interact with each other. The word "game" sounds playful, but it is meant
seriously. In fact, one of the early applications of game theory was in
deciding nuclear strategy.

If I'm writing a function, that's the <dfn>game</dfn> I find myself in. I call
this situation a game because it has these three aspects:

1. <dfn>Rules</dfn>: the programming language I use, the time I have available,
   the existing codebase, and my build system all constrain and define the
   game.

2. <dfn>Outcomes</dfn>: my code's correctness, quality, performance, and
   reusability might all vary, and some outcomes are better than others.

3. <dfn>Actions</dfn>: I must act to get the best outcome I know how to.

Sometimes I find it useful to think about life as a *set* of games. The insight
here is that we are always playing *multiple* games at very different scales:

- **Time**: Games repeat. A game can be *short-term* (a hackathon project,
  shipping an urgent feature) or *long-term* (making a flagship product,
  paying down technical debt).

- **Space**: Others are playing games too. A game can be *individual* (solo
  projects, low-level [IC] work) or *social* (collaborative projects,
  high-level IC work).

- **Scope**: Games are deeply nested. A given game might include *lower* games
  (typing quickly, naming a variable, reading API documentation) and be
  included within *higher* games (creating a great product, keeping my team
  happy, having pride in my craft).

[IC]: https://www.indeed.com/career-advice/finding-a-job/what-is-an-individual-contributor

<dfn>Fundamentals</dfn> are principles that apply to games across time, space,
and scope. They are important because they affect the entire set of games we
play.


## Finding fundamentals

At the broadest level, every game you play is constrained by reality, human
nature, and your own self-nature. So all you need to do is find the deep
principles that characterize all of reality and humankind.

Easy, right?

I can think of a few heuristics here:

- The *top-down* approach is to start with a formal theory (like game theory)
  and find rules that seem to apply to simple games. Then we can see how well
  those rules apply in practice.

- The *bottom-up* approach is to try what seems like it should work and see if
  it helps or not. If you do this for long enough -- across different domains,
  eras, and cultures -- then what survives is probably what's fundamental.

One ancient idea is to **live in reality**, which I think is the most important
fundamental of all:

- Great startups make something people want, not what they *think* people
  want.

- Great scientists rigorously test their ideas and keep only the ones that
  survive.

- Great relationships are about being authentic and dealing with who the other
  person is, not who we *assume* they are.

- Great people face their shortcomings honestly and address them. To paraphrase
  Fred Rogers, what is mentionable is manageable.

 
## Why fundamentals are simple

As principles become more fundamental, they inevitably lose detail and become 
simpler and more essential. Three scenarios:

- Your high-end restaurant is losing money. You have great chefs and excellent
  equipment, but your ingredients are terrible.

- Your spam detector does well on your training data but struggles in
  production. You investigate and find that many of your training examples are
  mislabeled.

- Your team has done another deathmarch to make a deadline. All of your
  colleagues are getting burned out, and one of them privately tells you that
  he's leaving the company.

Garbage in, garbage out.


## Why fundamentals are neglected

Simple principles cut across multiple domains, so we've heard them our whole
lives. The most important ones instinctively sound like clichés, and their
meaning is so obvious that even young children can understand them. You don't
need any cleverness or intelligence to know what these fundamentals mean.

And it's precisely this quality that makes them feel childish, basic,
and embarrassing. How would you feel if you were rushing to finish a project
and someone told you "haste makes waste"? Even knowing better, I feel
stunned to think about someone saying that to me at work.

> On one level, we all know this stuff already [...] The trick is keeping the
> truth up-front in daily consciousness.
>
> -- David Foster Wallace, "This is Water"

The instinctual resistance is that there is surely a more clever and
interesting solution. And sometimes there is, especially in rapidly growing
fields. But I still think we should search for them only after mastering the
fundamentals.


## Why fundamentals are difficult

Fundamentals are abstract generalizations across many different domains. The
more applicable they are, the more abstract they become.

But go deeply enough into any domain and you'll find that it's *enormously*
complex. [John Salvatier][john] writes memorably about the unexpected level of
detail he found when building staircases with his father:

> It’s tempting to think ‘So what?’ and dismiss these details as incidental or
> specific to stair carpentry. And they *are* specific to stair carpentry;
> that’s what makes them details. But the existence of a surprising number of
> meaningful details is not specific to stairs. Surprising detail is a near
> universal property of getting up close and personal with reality.

[john]: http://johnsalvatier.org/blog/2017/reality-has-a-surprising-amount-of-detail

There's a clear tension here. The fundamental seems too abstract to work with
the details of the situation. Or in the worst case, the fundamental makes sense
from the perspective of a higher-level game that we don't understand *or
even know about*.

Again, the approaches that come to my mind are top-down and bottom up.

The *top-down* approach exhaustively applies a fundamental we trust. How do you
*live in reality* with software engineering? Maybe this means:

- knowing your values, interests, and aptitudes
- measuring ceaselessly: timelines, metrics, performance, hotspots
- checking that your work solves a real need
- vetting your logic with unit and integration tests
- documenting our project to clarify our APIs and design goals
- mastering your project's languages and infrastructure
- understanding your project's costs and projected costs
- comparing your system to others and debating the trade-offs
- researching similar projects to learn about new breakthroughs
- scouting your company's competition
- asking your CEO to explain your company's business needs

The *bottom-up* approach tests a principle we're not sure about. How would a
skeptical person *live in reality* with software engineering? Maybe this means:

1. Ignore the principle and seeing how well that works.
2. Get experience by solving many different kinds of problems.
3. Introspect on what worked and what didn't.
4. Realize that the principle would have prevented a lot of headaches.
5. Apply the principle to new work with great success.
6. Declare that the principle is fundamental.

Either of these bring along multiple corollary values and skills: diligence,
courage, effort, persistence, organization, learning, practice, memorization,
communication, focus, social skills, creativity, measurement, objectivity,
patience, efficiency, speed, ...

But perhaps that should be its own post.


## Coda: Riffing on the games of life

As a parting thought, what I like about the "game" framing is that it neatly
includes a lot of big concepts. To riff on it a bit:

- Getting a good outcome is the <dfn>meaning</dfn> of a game.

- Choosing long-term games is <dfn>wisdom</dfn>.

- Low-level games are <dfn>tactics</dfn>. High-level games are
<dfn>strategy</dfn>.

- Social games are <dfn>culture</dfn>. Long-term culture is
  <dfn>tradition</dfn>.

- Games we choose subconsciously are <dfn>habits</dfn>. Subconscious cultural
  games are <dfn>deep culture</dfn>.

- The games a person plays with their own mental state are called <dfn>inner
  games</dfn>. High-level inner games are <dfn>spirituality</dfn>. In theory,
  the culture that supports spirituality is <dfn>religion</dfn>.

- The rules of the game are <dfn>reality</dfn>. The rules of the players are
  <dfn>human nature</dfn>. Our preferences among games and outcomes are our
  <dfn>values</dfn>. The actions available to us are our <dfn>ability</dfn>.
  Knowing which actions to use and which games to play is <dfn>judgment</dfn>.

- Values among low-level games are <dfn>likes and dislikes</dfn>. Values among
  mid-level games are <dfn>ethics</dfn>. Values among high-level games are
  <dfn>morals</dfn>. The sum total of our values is our <dfn>personality</dfn>.
  To reveal our highest games and values is <dfn>authenticity</dfn>.

- Discovering a new rule is <dfn>insight</dfn>.
