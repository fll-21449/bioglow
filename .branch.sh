PROGRAM=spike # valid choices are "spike" and "mindstorms"
PROGRAMS_BRANCH=programs-$(hostname | cut -d . -f 1)
PROGRAMS_REF=refs/heads/$PROGRAMS_BRANCH
