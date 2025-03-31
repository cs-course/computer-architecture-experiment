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

def calculate_miss_rate(hit_count, miss_count):
    if hit_count == 0:
        return float('inf')  # Handle division by zero
    return miss_count / (hit_count + miss_count)

def main():
    # Get trace file from command line argument or default to "traces/long.trace"
    trace = sys.argv[1] if len(sys.argv) > 1 else "traces/long.trace"
    
    # Print the header row
    print(f"Cache容量(KB),1路,2路,4路,8路")
    
    for i in range(1, 5):
        s = i + 4
        cache_capacity_kb = (2 ** (s - 5))
        outputs = [
            run_csim(s, 1, 5, trace),
            run_csim(s - 1, 2, 5, trace),
            run_csim(s - 2, 4, 5, trace),
            run_csim(s - 3, 8, 5, trace)
        ]
        
        miss_rates = []
        for output in outputs:
            formatted_output = process_output(output)
            hit_count, miss_count, eviction_count = map(int, formatted_output.split(','))
            miss_rate = calculate_miss_rate(hit_count, miss_count)
            miss_rates.append(miss_rate)
        
        # Print the cache capacity and corresponding miss rates
        print(f"{cache_capacity_kb},{miss_rates[0]:.3f},{miss_rates[1]:.3f},{miss_rates[2]:.3f},{miss_rates[3]:.3f}")

if __name__ == "__main__":
    main()