import random

def randomize_until_target(target, min, max):
    count = 0
    failed_results = []
    current_result = max

    while current_result > target:
        current_result = random.randint(min, max)
        failed_results.append(current_result)
        count += 1

    return count, failed_results

# Set the target value, min and max range here:
target_min = 1
target_max = 200
target_value = 50


for i in range(10):
    print(f"Trial #{i+1}:")
    result_count, failed_numbers = randomize_until_target(target_value, target_min, target_max)
    print(f"It took {result_count} attempts to reach the target value smaller or equal to {target_value}.")
    print(f"Failed numbers and correct final one: {failed_numbers}")
    print(f"______________________________")
