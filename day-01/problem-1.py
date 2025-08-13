filename = "input.txt"

data = []

# --- Step 1: Read the data and convert to integers ---
try:
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) != 2: continue
            try:
                data.append([int(parts[0]), int(parts[1])])
            except ValueError:
                print(f"Warning: Skipping non-integer line: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    exit()

if not data:
    print("No data was read from the file.")
    exit()

# --- Step 2: Separate the data into columns ---
columns = list(zip(*data))
col1 = list(columns[0])
col2 = list(columns[1])

# --- Step 3: Sort each column list independently ---
col1.sort()
col2.sort()

# --- Step 4: Calculate the difference for each pair ---
differences = []
# print("--- Calculating Individual Differences ---")
# zip the two sorted columns together to pair them up
for val1, val2 in zip(col1, col2):
    # abs() gives the absolute value (making the result positive)
    difference = abs(val1 - val2)
    differences.append(difference)
    # print(f"{val1}   {val2}   Difference: {difference}")

# --- Step 5: Sum all the differences ---
total_difference = sum(differences)

print("\n--- Final Result ---")
print(f"The sum of all differences is: {total_difference}")

