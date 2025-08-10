# The name of your input text file
filename = "input.txt"

# This list will hold your numeric data from the file
data = []

try:
    with open(filename, 'r') as file:
        for line in file:
            # Strip whitespace from the ends and split the line into parts.
            # .split() with no arguments handles one or more spaces as a delimiter.
            parts = line.strip().split()

            # Skip blank lines or lines that don't have exactly two columns
            if len(parts) != 2:
                continue

            try:
                # Convert the two parts to floating-point numbers
                col1 = float(parts[0])
                col2 = float(parts[1])
                # Append the pair of numbers to our data list
                data.append([col1, col2])
            except ValueError:
                # This line will be skipped if the parts are not valid numbers
                print(f"Warning: Skipping non-numeric line: {line.strip()}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    exit()

# --- The Core Sorting Logic ---
# sorted() creates a new sorted list.
# The 'key' argument defines what to sort by.
# 'lambda row: (row[0], row[1])' tells Python to sort using the first element
# of the row, and then use the second element to break any ties.
sorted_data = sorted(data, key=lambda row: (row[0], row[1]))

# --- Display the Result ---
print("--- Sorted Data ---")
for row in sorted_data:
    print(row)
