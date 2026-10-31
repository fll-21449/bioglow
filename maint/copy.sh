#!/bin/sh
#/ Usage: ./copy.sh
#/
#/ Copy programs-$host to the clipboard.

set -e
set -o nounset

source .branch.sh
set -x
git show $PROGRAMS_BRANCH:bioglow.py | pbcopy
