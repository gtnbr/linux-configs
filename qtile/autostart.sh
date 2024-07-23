#!/bin/sh
xrandr --output Virtual-1 --mode 1920x1080
nitrogen --restore &
picom &
qtile cmd-obj-o cmd -f reload_config