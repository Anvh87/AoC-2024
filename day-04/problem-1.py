def find_all_matches(grid, word):
    """
    Finds all occurrences of a word in a grid across all 8
    straight-line directions, counting each physical word once.
    """
    found = []
    if not grid:
        return found

    num_rows = len(grid)
    num_cols = len(grid[0])
    word_len = len(word)

    # Define all 8 directions (row_change, col_change)
    directions = [
        (0, 1), (0, -1),  # Right, Left
        (1, 0), (-1, 0),  # Down, Up
        (1, 1), (1, -1),  # Down-Right, Down-Left
        (-1, 1), (-1, -1)  # Up-Right, Up-Left
    ]

    # Iterate through every cell as a potential start point
    for r_start in range(num_rows):
        for c_start in range(num_cols):
            # Check if the starting letter matches
            if grid[r_start][c_start] == word[0]:
                # Check in all 8 directions
                for dr, dc in directions:
                    match_found = True
                    # Check the rest of the letters
                    for i in range(1, word_len):
                        r_next, c_next = r_start + i * dr, c_start + i * dc

                        if not (0 <= r_next < num_rows and 0 <= c_next < num_cols) or \
                                grid[r_next][c_next] != word[i]:
                            match_found = False
                            break

                    if match_found:
                        found.append({
                            "start": (r_start, c_start),
                            "direction": (dr, dc)
                        })
    return found


# --- Main Program ---

INPUT_FILE = "input.txt"
WORD_TO_FIND = "XMAS"
grid = []

try:
    with open(INPUT_FILE, 'r') as f:
        grid = [line.strip().upper() for line in f if line.strip()]
except FileNotFoundError:
    print(f"Error: The file '{INPUT_FILE}' was not found. Please create it.")
    exit()

if grid:
    all_matches = find_all_matches(grid, WORD_TO_FIND)

    for match in all_matches:
        # The 'word' key is removed as we only search for "XMAS" now
        print(f"- Found 'XMAS' starting at {match['start']} moving in direction {match['direction']}")

    print(f"Total matches found: {len(all_matches)}\n")

else:
    print(f"Error: The file '{INPUT_FILE}' is empty or could not be read.")