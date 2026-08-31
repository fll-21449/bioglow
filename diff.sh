#!/bin/bash
#/ Usage: ./diff.sh
#/
#/ Compare the latest version commited to the programs-$host branch with
#/ what's in the app.

set -e
set -o nounset

source .branch.sh

set -x
exec mind-meld $PROGRAM diff $PROGRAMS_REF
