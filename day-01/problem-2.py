import collections

filename = "input.text"

left_column = []
right_column = []

# --- Step 1: Read the original data into two separate lists ---
try:
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) != 2: continue
            try:
                left_column.append(int(parts[0]))
                right_column.append(int(parts[1]))
            except ValueError:
                print(f"Warning: Skipping non-integer line: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    exit()

if not left_column:
    print("No data was read from the file.")
    exit()

# --- Step 2: Create an efficient frequency count of the right column ---
# collections.Counter is a special dictionary perfect for counting things.
right_counts = collections.Counter(right_column)

# --- Step 3: Iterate through the left column and calculate ---
total_sum = 0
# print("--- Individual Calculations ---")
for number in left_column:
    # Get the count of the current number from our lookup table.
    # If the number isn't in the table, Counter defaults to 0.
    count = right_counts[number]
    
    product = number * count
    
    # Add the result to our running total
    total_sum += product
    
    # print(f"{number} * {count} = {product}")


# --- Step 4: Display the final result ---
print("\n--- Final Result ---")
print(f"The sum of all results is: {total_sum}")
