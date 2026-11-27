# What I learned

I came into this comfortable with Python but having never connected anything to the outside world — I'd never built an API integration, set up a webhook, or used a database for anything real. I learned all of it by building this bot in small steps, and these pages are a reflection on what actually stuck, roughly in the order it started to make sense to me.

A couple of ideas ran through the whole project. The biggest was to build in a deliberate order: get the plumbing working and verifiable before adding anything clever — a repo, then a server that runs, then one that can receive, then one that replies, and only then the actual logic. Every step ended in something I could check, so I was never debugging five new things at once.

The other is to avoid tying yourself to things you don't control. Partway in, Meta's WhatsApp setup locked me out behind business verification I couldn't complete, and instead of fighting it I moved the whole bot to Telegram in an afternoon — because I'd kept the messaging channel separate from the logic, so swapping it was cheap. That separation turned out to be the most useful decision I made.

The rest is grouped by topic:

- [APIs & HTTP](learnings/apis.md) — how programs talk to each other
- [Webhooks & networking](learnings/webhooks.md) — how Telegram reaches my laptop
- [Databases & SQL](learnings/databases.md) — how the bot remembers
- [LLMs](learnings/llms.md) — the part that understands and answers
- [Secrets, Git & tooling](learnings/tooling.md) — the workflow around it all
