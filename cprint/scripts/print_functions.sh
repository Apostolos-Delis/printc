#!/usr/bin/env bash

ansi()          { echo -e "\e[${1}m${*:2}\e[0m"; }
bold()          { ansi 1 "$@"; }
italic()        { ansi 3 "$@"; }
underline()     { ansi 4 "$@"; }
strikethrough() { ansi 9 "$@"; }
red()           { ansi 31 "$@"; }
green()         { ansi 32 "$@"; }
yellow()        { ansi 33 "$@"; }
blue()          { ansi 34 "$@"; }
purple()        { ansi 35 "$@"; }
cyan()          { ansi 36 "$@"; }
grey()          { ansi 37 "$@"; }
nocolor()       { ansi 38 "$@"; }
nocolor2()      { ansi 39 "$@"; }
whitebg()       { ansi 40 "$@"; }
redbg()         { ansi 41 "$@"; }


bold $1
italic $1
underline $1
strikethrough $1
red $1
green $1
yellow $1
blue $1
purple $1
cyan $1
grey $1
nocolor $1
nocolor2 $1
whitebg $1
redbg $1