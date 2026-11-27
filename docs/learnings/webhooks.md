# Webhooks & networking

There are two ways to get messages from Telegram, and the difference is who does the work. I could *poll* — keep asking "anything new?" over and over — or I could set up a webhook and have Telegram push each message to me the instant it arrives. The webhook is the better deal: instead of me pestering them, they call me.

But "they call me" raises a question I hadn't thought about — call me *where*? A webhook is an endpoint I host: a URL Telegram sends each new message to. Which means the roles flip. Normally my code is the client calling Telegram, but for the webhook, Telegram is the client and my little server is the one being called. And Telegram doesn't learn anything about my setup — it just sends a fixed, documented shape to whatever URL I register, and it's on me to read it.

One thing I only really understood by watching it happen: a webhook wants a quick "200 OK" back, and if it doesn't get one it assumes delivery failed and retries later. At one point my connection was slow, messages piled up, and the moment it recovered a burst of them flushed through all at once. That was the retry behaviour, live.

Because that URL is public, anything could POST to it pretending to be Telegram. So I register a secret token, Telegram echoes it back in a header on every request, and my code checks it — anything that doesn't match gets rejected with a 403. (The message itself rides in the request body; the secret rides in a header — two different parts of the same request.)

The part that genuinely surprised me was realising my laptop can't just be reached from the internet. It sits behind my router on a private address, and the router blocks anything trying to start a conversation from outside. Outbound works — that's why I can browse and send API calls — but nothing can reach *in*. So how does a webhook get to a server running on my own machine?

That's what ngrok is for. It opens an outbound connection from my laptop to its own public server, then relays anything that hits that public URL back down to me — a temporary stand-in for a real address, just for development. When you actually deploy, a host runs your code on a machine that already has its own public address, and the tunnel isn't needed anymore.

A few smaller things settled along the way: `localhost` and `127.0.0.1` are the same thing, just "this computer"; and one machine has many ports — numbered doors, one per program (my server on 8000, ngrok's inspector on 4040). And when a `curl` once timed out with "failed to connect", I learned to read that as a network problem rather than a bug — my home wifi was quietly blocking Telegram, and a phone hotspot fixed it.
