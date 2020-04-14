printf "         Your simulator\n"
printf "(s,E,b)  %-10s %-10s %-10s\n" Hits Misses Evicts
while read s e b t; do
    printf "(%s,%s,%s)  %-10s %-10s %-10s  %s\n" $s $e $b \
        `./csim -s $s -E $e -b $b -t $t | sed 's/[^0-9 ]*//g'` \
        $t
done <<< \
"""1 1 1 traces/yi2.trace
4 2 4 traces/yi.trace
2 1 4 traces/dave.trace
2 1 3 traces/trans.trace
2 2 3 traces/trans.trace
2 4 3 traces/trans.trace
5 1 5 traces/trans.trace
5 1 5 traces/long.trace"""
