#!/usr/bin/env bash


RED='\033[0;31m'
NC='\033[0;0m'
BLUE='\033[0;34'

case $1 in
"BLUE")
    color='\033[0;34m'
    ;;
"RED")
    color='\033[0;31m'
    ;;
"NC")
    color='\033[0;0m'
    ;;
esac

all="${@:2}"
#
#echo -e "\e[1m$all\e[0m"
#echo -e "Normal \e[5mBlink"
#echo -e "Normal \e[7minverted${NC}"

echo -e "${color}$all ${NC}"
#
#ansi()          { echo -e "\e[${1}m${*:2}\e[0m"; }
#bold()          { ansi 1 "$@"; }
#italic()        { ansi 3 "$@"; }
#underline()     { ansi 4 "$@"; }
#strikethrough() { ansi 9 "$@"; }
#red()           { ansi 31 "$@"; }
#green()         { ansi 32 "$@"; }
#yellow()        { ansi 33 "$@"; }
#blue()          { ansi 34 "$@"; }
#purple()        { ansi 35 "$@"; }
#cyan()          { ansi 36 "$@"; }
#grey()          { ansi 37 "$@"; }
#nocolor()       { ansi 38 "$@"; }
#nocolor2()      { ansi 39 "$@"; }
#whitebg()       { ansi 40 "$@"; }
#redbg()         { ansi 41 "$@"; }
#greenbg()         { ansi 42 "$@"; }
#yellowbg()         { ansi 43 "$@"; }
#bluebg()         { ansi 44 "$@"; }
#purplebg()         { ansi 45 "$@"; }
#turquiosbg()    { ansi 46 "$@"; }
#test6()         { ansi 47 "$@"; }
#test7()         { ansi 48 "$@"; }
#test8()         { ansi 49 "$@"; }
#test9()         { ansi 50 "$@"; }
#test10()         { ansi 51 "$@"; }
#
#
#
#bold $1
#italic $1
#underline $1
#strikethrough $1
#red $1
#green $1
#yellow $1
#blue $1
#purple $1
#cyan $1
#grey $1
#nocolor $1
#nocolor2 $1
#whitebg $1
#redbg $1
##test1 $1
##test2 $1
##test3 $1
##test4 $1
##test5 $1
##test6 $1
##test7 $1
##test8 $1
##test9 $1
##test10 $1
#printf "$font=italic italic"
