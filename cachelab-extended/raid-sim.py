# To simulate the disk array system, we can use a Monte Carlo simulation approach.
# We can simulate the failure of each disk using a Bernoulli distribution with a probability of 0.1%.
# We can then check if any disk has failed and if so, consider the entire array to have failed.
# We can repeat this simulation many times and calculate the average time until failure to estimate the MTTF.

import random

num_disks = 5
annual_failure_prob = 0.05

def simulate_disk_failure():
    """Simulate the failure of a single disk."""
    return random.random() < annual_failure_prob

def simulate_array_failure():
    """Simulate the failure of the entire array."""
    if sum([simulate_disk_failure() for i in range(num_disks)]) >= 1:
        return True
    return False

def simulate_mtff(num_simulations):
    """Simulate the MTTF of the array using the given number of simulations."""
    total_time_until_failure = 0
    for i in range(num_simulations):
        if simulate_array_failure():
            total_time_until_failure += 1
    return num_simulations / total_time_until_failure

# Example usage:
mttf = simulate_mtff(80000)
print("Estimated MTTF:", mttf)
