This is a mirror of [the CodeFenceCleanup
gist](https://gist.github.com/EliahKagan/16a6b13ee717149ab41f983b3635659c).
This repository might be easier to read and work with, but their contents are
the same except internal hyperlinks.

---

# CodeFenceCleanup - scripts for finding posts with broken code fences

*Written in 2020 by Eliah Kagan \<degeneracypressure@gmail.com\>.*

*To the extent possible under law, the author(s) have dedicated all copyright
and related and neighboring rights to this software to the public domain
worldwide. This software is distributed without any warranty.*

*You should have received a copy of the CC0 Public Domain Dedication along with
this software. If not, see
<http://creativecommons.org/publicdomain/zero/1.0/>.*

These are scripts for finding [broken code
fences](https://chat.stackexchange.com/transcript/3877?m=54555504#54555504).

(This is intended to supersede [that gist, which is less
complete](https://gist.github.com/EliahKagan/3d764c8099c7b652e1c2c01ee02dadaa).)

This is based on another repository (from which that gist is also copied). This
is rebased to omit .csv files that were obtained from
[SEDE](https://data.stackexchange.com/). Those files could probably be
redistributed, but under the appropriate CC licenses for user-contributed
content on Stack Exchange, *not* under this public domain dedication. *To my
recollection*, that repository was never published.

I believe I did the rebase correctly, but in case some commit has a .csv file,
I am *not* claiming authorship of its contents, nor attempting to offer it
under CC0.

---

**The only script here that is currently being used is
[`filter-fences`](filter-fences).**

To use it, give it CSV data on standard input. For example:

```sh
./filter-fences <QueryResults.csv >outfile
```

Previous versions of `filter-fences` hard-coded the input filename (and did not
read from standard input), but the current version works this way instead.

The other script that was once useful is `expand.py`, but that approach to
generating T-SQL is no longer being used. Instead, [a more general (and much
nicer)
query](https://data.stackexchange.com/askubuntu/revision/1246925/1535442/seems-to-have-code-fences)
is used and filtered (way!) down by `filter-fences`.

The other script, `search.py`, is just a bit of scratchwork.
