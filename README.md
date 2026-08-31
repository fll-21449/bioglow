# Rocket Fish programs for Unearthed season

We're trying Python this season. This repo tracks our code changes throughout the season.

## Synopsis

1. Install mind-meld from a
   [release](https://github.com/spraints/mind-meld/releases/tag/v0.2.0) or by
   running `go install github.com/spraints/mind-meld@latest`.

1. Sync from the LEGO app to this repo (locally and to GitHub).

    ```
    ./sync.sh
    ```
    
1. View the programs on the
   [programs](https://github.com/fll-21449/bioglow/tree/programs) branch.

Optionally, run `./diff.sh` to see what has changed since the last sync.

## Full workflow

Here's how we usually use this at meetings.

* At the start of the meeting, run `./diff.sh`. If it shows any differences,
  run `./sync.sh -m 'start of meeting'`.

* At the end of the meeting, or if there's a significant save point, run
  `./sync.sh -m 'blah blah'` to save a copy of the current programs.

* Between meetings, merge together all of the programs.

    - `maint/merge.sh` fetches all `programs-$host` branches from github and
      merges them together into a `programs` branch. If the merge fails because
      of conflicts: resolve the conflicts, commit the result, run `git checkout
      main`, then run `maint/merge.sh` again.

    - Copy the merged program into the app.

	- `maint/ff.sh` updates this computer's `programs-$host` branch to
	  match the combined `programs` branch. This only works if `programs`
          includes all of the commits from `programs-$host`.

	- `./diff.sh` shows a reverse diff of the changes we're about to apply.
	  Make sure that the `-` lines look like what you expect to be bringing
          in from the other computer(s).

	- `git show programs-$host:bioglow.py | pbcopy` and then paste into the
	  app. Run `./diff.sh`, there should be no differences.  If there are,
	  they are most likely just whitespace differences. (The app strips out
	  some meaningless whitespace when you paste into it.) I usually add
          the extra whitespace so that the diff is clean.
