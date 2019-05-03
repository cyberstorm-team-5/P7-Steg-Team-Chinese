#!/bin/bash

#USAGE: ./bash-steg.sh (bB) (o-start) (o-end) (wrapper file) (i-start) (i-end)

#example: ./bash-steg.sh B 1023 1027 stegged-byte.bmp 5 8
oStart=$(($2 + 0))
oEnd=$(($3 + 0))
iStart=$5
iEnd=$6


#byte method
if [ "$1" == "B" ]; then 

    for o in $(seq $oStart $oEnd)
    do
        for i in $(seq $iStart $iEnd)
        do
            #NOTE: prints out offset and interval in name on top each other in order of offsetInterval
            ./steg.py -B -r -o$o -i$i -w$4 > B_oi$o$i
        done    
    done

#bit method
else
    for o in $(seq $oStart $oEnd)
    do
        ./steg.py -b -r -o$o -w$4 > b_o$o
    done
fi
