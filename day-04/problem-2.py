def find_flexible_mas_pattern(grid):
    """
    Finds a full "X" pattern where both diagonals spell "MAS"
    starting from any corner.
    """
    count = 0
    if not grid or len(grid) < 3:
        return 0

    num_rows = len(grid)
    num_cols = len(grid[0])

    # The required letters for each diagonal pair
    target_corners = {'M', 'S'}

    # Iterate through the inner grid to find a potential 'A' center
    for r in range(1, num_rows - 1):
        for c in range(1, num_cols - 1):
            if grid[r][c] == 'A':
                # Get all four corner characters
                tl_char = grid[r - 1][c - 1]  # Top-Left
                br_char = grid[r + 1][c + 1]  # Bottom-Right
                tr_char = grid[r - 1][c + 1]  # Top-Right
                bl_char = grid[r + 1][c - 1]  # Bottom-Left

                # Check if the first diagonal's corners are {M, S}
                is_diag1_valid = {tl_char, br_char} == target_corners

                # Check if the second diagonal's corners are also {M, S}
                is_diag2_valid = {tr_char, bl_char} == target_corners

                # If both are valid, it's a match
                if is_diag1_valid and is_diag2_valid:
                    count += 1

    return count


# --- Main Program ---

INPUT_FILE = "input.txt"
grid = []

# 1. Read the grid from the input file
try:
    with open(INPUT_FILE, 'r') as f:
        # Read each line, strip whitespace, and build the grid list
        grid = [line.strip().upper() for line in f if line.strip()]
except FileNotFoundError:
    print(f"Error: The file '{INPUT_FILE}' was not found. Please create it.")
    exit()

# 2. Run the search and print the final count
if grid:
    match_count = find_flexible_mas_pattern(grid)
    print(f"Total 'MAS' X-patterns found: {match_count}")
else:
    print(f"Error: The file '{INPUT_FILE}' is empty or could not be read.")