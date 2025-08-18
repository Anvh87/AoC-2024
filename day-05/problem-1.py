def validate_sequences_and_sum_middle(file_path: str):
    """
    Reads a file containing ordering rules and data sequences, prints the
    sequences that conform to all rules, and calculates the sum of their
    middle numbers.

    Args:
        file_path (str): The path to the input file.
    """
    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return

    try:
        rules_section, data_section = content.strip().split('\n\n')
    except ValueError:
        print("Error: The input file must have a rules section and a data section separated by a blank line.")
        return

    # --- 1. Parse the Rules ---
    rules = []
    for line in rules_section.strip().split('\n'):
        if '|' in line:
            try:
                before, after = line.strip().split('|')
                rules.append((int(before), int(after)))
            except ValueError:
                print(f"Warning: Skipping malformed rule line: '{line}'")

    print("--- Rules Loaded ---")
    print(f"Found {len(rules)} rules to apply.")
    print("\n--- Valid Sequences ---")

    # --- 2. Process, Validate, and Calculate Total ---
    data_rows = data_section.strip().split('\n')

    # Initialize a variable to store the sum of the middle numbers
    middle_number_total = 0

    for row_string in data_rows:
        try:
            sequence = [int(num) for num in row_string.strip().split(',')]
        except ValueError:
            print(f"Warning: Skipping malformed data row: '{row_string}'")
            continue

        is_valid = True
        for before_val, after_val in rules:
            if before_val in sequence and after_val in sequence:
                if sequence.index(before_val) > sequence.index(after_val):
                    is_valid = False
                    break

        if is_valid:
            print(row_string)
            # Find the middle index of the sequence.
            # Integer division `//` handles both even and odd lengths correctly.
            middle_index = len(sequence) // 2
            middle_number = sequence[middle_index]

            # Add the middle number to our running total
            middle_number_total += middle_number

    # --- 3. Print the Final Total ---
    print("\n--- Calculation Complete ---")
    print(f"Total of middle numbers: {middle_number_total}")


# --- Main execution block ---
if __name__ == "__main__":
    INPUT_FILE = "input.txt"
    validate_sequences_and_sum_middle(INPUT_FILE)