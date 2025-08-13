import numpy as np


def analyze_sequence(arr):

    # A valid sequence needs at least 2 numbers to have a difference.
    if arr.size < 2:
        return "insufficient data"

    diffs = np.diff(arr)

    # Check for constrained ascending or descending
    is_ascending = np.all((diffs >= 1) & (diffs <= 3))
    is_descending = np.all((diffs >= -3) & (diffs <= -1))

    if is_ascending:
        return 'constrained ascending'
    elif is_descending:
        return 'constrained descending'
    else:
        return 'unordered or fails constraints'


def find_safe_sequence(arr):

    # 1. First, check if the original sequence is already valid.
    initial_result = analyze_sequence(arr)
    if 'constrained' in initial_result:
        return 'Safe', 'original is valid'

    # 2. If not, try removing each number one at a time.
    for i in range(arr.size):
        # Create a new temporary array with one element removed
        temp_arr = np.delete(arr, i)

        # Check if this new, shorter sequence is valid
        temp_result = analyze_sequence(temp_arr)
        if 'constrained' in temp_result:
            return 'Safe', f"by removing '{arr[i]}' at index {i}"

    # 3. If no single removal creates a valid sequence, it's unsafe.
    return 'Unsafe', 'no single removal works'


# --- Main script execution ---

# Initialize counters
safe_count = 0
unsafe_count = 0
file_path = 'input.txt'

print(f"--- Analyzing data from '{file_path}' with new rules ---")

try:
    with open(file_path, 'r') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue

            try:
                numbers = np.array([int(n) for n in line.split()])

                if numbers.size < 3:  # Need at least 3 numbers to be able to remove one and still check
                    print(f"Line {line_num}: {numbers} -> Skipped (not enough data for removal test)")
                    continue

                # Get the status ('Safe' or 'Unsafe') and the reason
                status, reason = find_safe_sequence(numbers)
                print(f"Line {line_num}: {numbers} -> {status} ({reason})")

                # Update counters based on the status
                if status == 'Safe':
                    safe_count += 1
                else:
                    unsafe_count += 1

            except ValueError:
                print(f"Line {line_num}: Skipped due to invalid non-numeric data ('{line}')")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")

# Print the final summary
print("\n--- Challenge Analysis Complete ---")
print(f"Total Safe Sequences: {safe_count} ✅")
print(f"Total Unsafe Sequences: {unsafe_count} ❌")