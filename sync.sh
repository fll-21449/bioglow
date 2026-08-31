#!/bin/bash
#/ Usage: ./sync.sh [-m MESSAGE]
#/
#/ Make a copy of the current programs on the 'programs-$host' branch and push
#/ to github.

set -e
set -o nounset

. .branch.sh
UPSTREAM_BRANCH=programs

if git cat-file -e $UPSTREAM_BRANCH >&/dev/null && ! git cat-file -e $PROGRAMS_REF >&/dev/null; then
  (set -x; git update-ref $PROGRAMS_REF $UPSTREAM_BRANCH)
fi

set -x
mind-meld $PROGRAM fetch --git $PROGRAMS_REF "$@"
git push origin $PROGRAMS_BRANCH
