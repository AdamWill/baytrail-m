#!/bin/bash

# Based on an original by Maxwell Pray (synthead), from
# https://bbs.archlinux.org/viewtopic.php?id=107167

xinputs=( 9 10 )

xrandrout="$(xrandr)"

case $xrandrout in
 *1280?x?800* ) rotate=0;;
 *800?x?1280* ) rotate=1;;
esac

xrandr -o $(( rotate * 3 ))

# Seems to be working automatically since kernel 3.14rc3 or so. This script
# is really now just a convenience call to xrandr.
#for input in ${xinputs[@]}; do
# xinput set-prop $input "Evdev Axes Swap" $rotate
# xinput set-prop $input "Evdev Axis Inversion" 0, $rotate
#done
