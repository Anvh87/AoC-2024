filename = "input.text"
data = []

# --- Step 1: Read the data from the file (same as before) ---
try:
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) != 2: continue
            try:
                data.append([int(parts[0]), int(parts[1])])
            except ValueError:
                print(f"Warning: Skipping non-numeric line: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    exit()

# --- Step 2: Separate the data into columns ---
# zip(*data) is a Python idiom to transpose a list of lists.
# It groups the first elements together, the second elements together, etc.
if data:
    columns = list(zip(*data))
    col1 = list(columns[0])
    col2 = list(columns[1])

    # --- Step 3: Sort each column list independently ---
    col1.sort()
    col2.sort()

    # --- Step 4: Display the results ---
    print("--- Sorted Columns as Separate Lists ---")
    print("Column 1 sorted:", col1)
    print("Column 2 sorted:", col2)

    print("\n--- Sorted Columns Recombined into a Table ---")
    # zip() them back together to display them row by row
    sorted_recombined = list(zip(col1, col2))
    for row in sorted_recombined:
        print(row)
else:
    print("No data was read from the file.")

