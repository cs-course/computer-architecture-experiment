trace=$1
if [ -z $trace ]; then
    trace="traces/long.trace"
fi 
for i in {1..4}; do
  s=$((i + 4))
  ./csim.exe -s $s -E 1 -b 5 -t $trace  | sed -e 's/[^0-9 ]*//g' -e 's/ /,/g'
  ./csim.exe -s $((s - 1)) -E 2 -b 5 -t $trace | sed -e 's/[^0-9 ]*//g' -e 's/ /,/g'
  ./csim.exe -s $((s - 2)) -E 4 -b 5 -t $trace | sed -e 's/[^0-9 ]*//g' -e 's/ /,/g'
  ./csim.exe -s $((s - 3)) -E 8 -b 5 -t $trace | sed -e 's/[^0-9 ]*//g' -e 's/ /,/g'
done
