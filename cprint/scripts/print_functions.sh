#!/usr/bin/env bash


RED='\033[0;31m'
NC='\033[0;0m'
BLUE='\033[0;34m'

# Black        0;30     Dark Gray     1;30
# Red          0;31     Light Red     1;31
# Green        0;32     Light Green   1;32
# Brown/Orange 0;33     Yellow        1;33
# Blue         0;34     Light Blue    1;34
# Purple       0;35     Light Purple  1;35
# Cyan         0;36     Light Cyan    1;36
# Light Gray   0;37     White         1;37


case $1 in
"BLACK")
    color='\033[0;30m'
    ;;
"RED")
    color='\033[0;31m'
    ;;
"GREEN")
    color='\033[0;32m'
    ;;
"ORANGE")
    color='\033[0;33m'
    ;;
"BROWN")
    color='\033[0;33m'
    ;;
"BLUE")
    color='\033[0;34m'
    ;;
"PURPLE")
    color='\033[0;35m'
    ;;
"CYAN")
    color='\033[0;36m'
    ;;
"LIGHT GRAY")
    color='\033[0;37m'
    ;;
"DARK GRAY")
    color='\033[1;30m'
    ;;
"LIGHT RED")
    color='\033[1;31m'
    ;;
"LIGHT GREEN")
    color='\033[1;32m'
    ;;
"YELLOW")
    color='\033[1;33m'
    ;;
"LIGHT BLUE")
    color='\033[1;34m'
    ;;
"LIGHT PURPLE")
    color='\033[1;35m'
    ;;
"LIGHT CYAN")
    color='\033[1;36m'
    ;;
"WHITE")
    color='\033[1;37m'
    ;;
"NC")
    color='\033[0;0m'
    ;;
esac

all="${@:2}"

echo -e "${color}$all ${NC}"

#echo -e $'\e[32;1mbold red\e[0mplain\e[4munderlined'

#
#echo -e "\e[1m$all\e[0m"
#echo -e "Normal \e[5mBlink"
#echo -e "Normal \e[7minverted${NC}"
#
#echo -e "${color}$all ${NC}"
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
