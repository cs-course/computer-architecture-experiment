#!/bin/bash
printf "              Your simulator\n"
printf "     (s,E,b)  %10s %10s %10s\n" Hits Misses Evicts
while read s e b t r; do
    result=`./csim -s $s -E $e -b $b -t $t | sed 's/[^0-9 ]*//g'`
    [ "$result" == "$r" ] && printf "Pass " || printf "     "
    printf "(%s,%s,%s)  %10s %10s %10s  %s\n" $s $e $b $result $t
done <<< \
"""1 1 1 traces/yi2.trace 9 8 6
4 2 4 traces/yi.trace 4 5 2
2 1 4 traces/dave.trace 2 3 1
2 1 3 traces/trans.trace 167 71 67
2 2 3 traces/trans.trace 201 37 29
2 4 3 traces/trans.trace 212 26 10
5 1 5 traces/trans.trace 231 7 0
5 1 5 traces/long.trace 265189 21775 21743"""
