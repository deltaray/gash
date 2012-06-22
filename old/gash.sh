#!/bin/bash

# GASH v0.1 by Mark Krenz

# This program is not for use. Use the gash program written in
# Perl instead.

# This is the original shell script I wrote to test the gash concept.
# It worked, but I decided that running grep and other commands so much
# would work against my goal of keeping the execution time low. Plus,
# Plus it kinda limits my options for doing advanced processing and
# programming.


savefile=$HOME/.gash

# The return value from the last command is passed via argument in the
# PROMPT_COMMAND variable.
returnvalue=$1

if [ -s $savefile ]; then
    charvalues=( $( cat $savefile ) )
fi

level=${charvalues[0]:-1}
exp=${charvalues[1]:-0}
hp=${charvalues[2]:-6}
gold=${charvalues[3]:-50}

maxhp=$(( $level * 6 ))

lastmessage=""

cwd=$(pwd)


if [[ $hp == 0 ]]; then  # Elf shot the food and the wizard died.
    echo "You died! Press enter to create new character."
    read
    rm -f $savefile
    echo "Starting new character."

else # Normal game logic

    if [[ $( grep " " <<<$cwd ) ]]; then
        hp=$(( $hp - 1 ))
        lastmessage="The poisonous content of this directory pathname causes you 1 point of damage"
    fi

    if [[ $returnvalue == 0 ]]; then

        exp=$(( $exp + 1 ))

    elif [[ $returnvalue -gt 0 ]]; then
        hp=$(( $hp - 1 ))
         lastmessage="You where hit for 1 point damage"
    fi

    if [[ $hp -gt $maxhp ]]; then
        hp=$maxhp
    fi

    if [[ $exp != 0 && $(( $exp % $(( 100 * $level )) )) == 0 ]]; then
        level=$(( $level + 1 ))
        hp=$(( $level * 6 ))
        echo "+----------------------------------+"
        echo "|          LEVEL UP!!              |"
        echo "+----------------------------------+"
        echo "Next Level at $(( 100 * $level )) exp."

    fi


    printf "\e[37;40m| GASH level: %-4d exp: %-12s hp: %-5d gold: %-8d | %s \e[K\e[0m\n" $level "$exp / $(( 100 * $level ))" $hp $gold "$lastmessage"
#    echo $2 - $3 - $4 - $5

    echo "$level $exp $hp $gold" > $savefile

fi

