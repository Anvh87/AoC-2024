import numpy as np


def analyze_sequence(arr):

    diffs = np.diff(arr)

    # Check for constrained ascending
    if np.all((diffs >= 1) & (diffs <= 3)):
        return 'constrained ascending'

    # Check for constrained descending
    elif np.all((diffs >= -3) & (diffs <= -1)):
        return 'constrained descending'

    else:
        return 'unordered or fails constraints'


# --- Main script execution ---

# 1. Initialize counters
ascending_count = 0
descending_count = 0

try:
    with open('input.txt', 'r') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue

            try:
                numbers = np.array([int(n) for n in line.split()])

                if numbers.size < 2:
                    print(f"Line {line_num}: {numbers} -> insufficient data")
                    continue

                result = analyze_sequence(numbers)
                print(f"Line {line_num}: {numbers} -> {result}")

                # 2. Update counters based on the result
                if result == 'constrained ascending':
                    ascending_count += 1
                elif result == 'constrained descending':
                    descending_count += 1

            except ValueError:
                 print(f"Line {line_num}: Skipped due to invalid non-numeric data ('{line}')")

except FileNotFoundError:
    print(f"Error: The file was not found.")

# 3. Print the final summary
print("\n--- Analysis Complete ---")
print(f"Total Constrained Ascending: {ascending_count}")
print(f"Total Constrained Descending: {descending_count}")
print(f"Total Combined: {ascending_count + descending_count}")
