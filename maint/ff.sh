#!/bin/sh
#/ Usage: ./ff.sh
#/
#/ Update programs-$host to match programs, but only if programs has all of the
#/ changes from programs-$host.

set -e
set -o nounset

source .branch.sh

set -x
git fetch
git checkout $PROGRAMS_BRANCH
trap "git checkout -" EXIT
git merge --ff-only origin/programs
git push origin "$PROGRAMS_BRANCH"
