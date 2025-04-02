import subprocess
import sys
import re

def run_csim(s, E, b, trace):
    command = f"./csim -s {s} -E {E} -b {b} -t {trace}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def process_output(output):
    # Remove all non-numeric characters except spaces
    cleaned_output = re.sub(r'[^0-9 ]', '', output)
    # Replace spaces with commas
    formatted_output = re.sub(r'\s+', ',', cleaned_output.strip())
    return formatted_output

def main():
    # Get trace file from command line argument or default to "traces/long.trace"
    trace = sys.argv[1] if len(sys.argv) > 1 else "traces/long.trace"
    
    # Print the header row
    print(f"Cache容量(KB),16字节,32字节,64字节,128字节,256字节")
    
    # Define cache capacities and corresponding s values
    cache_capacities_kb = [1, 2, 4, 8]
    initial_s_values = [6, 7, 8, 9]  # s = log2(capacity in KB) + 4
    
    # Block sizes in bytes and corresponding b values
    block_sizes_b = [4, 5, 6, 7, 8]  # b = log2(block size in bytes)
    
    for cache_capacity_kb, initial_s in zip(cache_capacities_kb, initial_s_values):
        outputs = []
        for i, b in enumerate(block_sizes_b):
            s = initial_s - i  # Decrease s by 1 for each doubling of block size
            output = run_csim(s, 1, b, trace)
            outputs.append(output)
        
        miss_rates = []
        for output in outputs:
            formatted_output = process_output(output)
            if formatted_output:
                hit_count, miss_count, eviction_count = map(int, formatted_output.split(','))
                miss_rate = miss_count / (hit_count + miss_count)
                miss_rates.append(miss_rate)
            else:
                miss_rates.append(float('nan'))  # Handle cases where output is not as expected
        
        # Print the cache capacity and corresponding miss rates
        print(f"{cache_capacity_kb},{miss_rates[0]:.3f},{miss_rates[1]:.3f},{miss_rates[2]:.3f},{miss_rates[3]:.3f},{miss_rates[4]:.3f}")

if __name__ == "__main__":
    main()