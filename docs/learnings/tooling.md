# Secrets, Git & tooling

This is the scaffolding around the actual bot — the habits and tools that make it a real project rather than a throwaway script.

## Secrets

The one rule I drilled into myself: secrets never go in the code or the repo. The bot token and API keys live in a `.env` file that git ignores, and the code reads them from the environment at runtime. I commit a `.env.example` with the names but no values, so anyone cloning the repo knows what to supply. I also learned to check `git status` *before* committing — and that if a secret ever leaks, you rotate it immediately rather than hope nobody noticed (I did exactly that after pasting my bot token by accident). For generating one, `openssl rand -hex 32` gives you something genuinely unguessable.

## Git, and juggling two accounts

What finally clarified git for me was separating two "identities" I'd been treating as one. There's *who wrote a commit* (set with `git config user.name/email`), and there's *which account is allowed to push* (handled by SSH keys). I keep separate work and personal GitHub accounts, so I use an SSH host alias to make sure pushes from this project land on the personal one, plus a GitHub noreply email to keep my real address out of public history. And it all stays local until you push — `init`, `add`, `commit` happen on my machine; GitHub only hears about it when I push.

## Python and the toolchain

Poetry manages the project's dependencies and its virtual environment — an isolated set of packages just for this project, so it never clashes with anything else, with exact versions pinned so the setup is reproducible. A few smaller things I now actually understand rather than copy: `poetry run` executes a command inside that environment; `__init__.py` marks a folder as an importable package; and an import like `expense_bot.db` means the `db.py` module inside the `expense_bot` package — not to be confused with `expenses.db`, which is the data file.

## FastAPI

FastAPI is the framework that receives requests; uvicorn is the server that runs it and listens on a port — the recipe and the cook. A route like `@app.get("/health")` just registers a function to handle requests to that path. The neat part is that FastAPI fills in your function's arguments from the right place based on their type — a `dict` comes from the request body, a header from `Header(...)` — so you declare what you want and it hands it over. It also generates interactive API docs at `/docs` for free.

## The terminal

Most of my friction was the shell, not the code. I learned to quote URLs so characters like `?` and `&` aren't misread, that `< >` and `[]` mean special things to the shell, and that a long one-liner pastes more reliably than a multi-line command. The `curl` flags make sense now too: `-X` sets the method, `-H` adds a header, `-d` sends a body. Small stuff, but it's the difference between fighting the terminal and using it.
