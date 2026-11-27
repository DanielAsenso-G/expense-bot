# Databases & SQL

The bot was useless until it could remember things. Before that, anything it "knew" lived in memory and vanished the moment the program restarted — RAM is temporary. To remember expenses across days, I had to write them to disk, and a database is just an organised way to do that.

The model that made databases click was a spreadsheet. A database holds tables; a table has columns (the fields — amount, category, a note, a date) and rows (one per expense). The shape of those columns is the schema, and you talk to the whole thing in SQL, a language that reads almost like English (`SELECT`, `INSERT`, and so on).

I used SQLite, which is a full database that lives in a single file with no separate server to run — the same thing that quietly runs inside phones and browsers. The alternative, something like Postgres, runs as its own service that many apps connect to over a network; that's what you reach for once you have lots of users (and you'd add a column to tag whose data is whose). For one person and one file, SQLite is perfect.

The most useful habit I picked up was designing the table *backwards from the questions I'd ask it*. I knew I'd want "how much, on what, and when", so the columns almost wrote themselves. I also learned to be deliberate about constraints — amount and category are required, but the note is optional, so I left it nullable.

Two things about writing to it stuck with me. First, changes aren't saved until you `commit()` — until then they're staged, a bit like edits you haven't hit save on. Second, you never paste values straight into a SQL string. If you did, a mischievous note like `'); DROP TABLE expenses;--` could be read as a *command* and wipe the table — that's SQL injection. Instead you leave `?` placeholders and hand the values over separately, so the database always treats them as data, never code (it also quietly handles awkward characters like apostrophes, which would otherwise break the query).

Reading data back introduced the cursor — running a `SELECT` hands you a pointer into the results that you pull rows out of with `fetchall()`. The one trap I hit: you have to fetch the rows *before* you close the connection, because the cursor reads from the connection you just shut.

I also brushed up against migrations — the idea that once a table holds real data, you can't just rewrite its definition; you change it carefully with `ALTER TABLE` so you don't lose what's there. I didn't need one this time, but it's good to know the live schema isn't something you edit casually.
