#!/bin/bash
#/ Usage: maint/merge.sh
#/
#/ Merge all programs-$host branches into a combined programs branch. If there
#/ is an error, it will stop and leave everything in a dirty state so that you
#/ can finish the merge manually.

set -e
set -o nounset

(set -x; git fetch)

if ! git cat-file -e origin/programs; then
  echo "The 'programs' branch is missing from GitHub. You must create it from"
  echo "a known good starting point before using this script."
  exit 1
fi

host_branches="$(git for-each-ref 'refs/remotes/origin/programs-*' | cut -d / -f 3-)"

if [ -z "$host_branches" ]; then
  echo "No per-host programs found. You must run ./sync.sh from at least one"
  echo "computer before using this script."
  exit 1
fi

set -x
(set -x; git checkout programs)
(set -x; git merge --ff-only origin/programs) || { echo "+++++ abort +++++"; (set -x; git checkout -) }
(set -x; git merge $host_branches)
(set -x; git push origin programs)
(set -x; git checkout -)
echo 'OK!'
