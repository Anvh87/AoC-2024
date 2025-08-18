import collections


def topological_sort(sequence_to_sort: list, all_rules: list):
    """
    Reorders a sequence of numbers based on a set of ordering rules using a
    topological sort (Kahn's algorithm).

    Args:
        sequence_to_sort (list): The list of numbers to reorder.
        all_rules (list): A list of all rule tuples, e.g., [(before, after), ...].

    Returns:
        list: The correctly sorted list of numbers, or None if a circular
              dependency (a cycle) makes sorting impossible.
    """
    nodes = set(sequence_to_sort)
    graph = {node: [] for node in nodes}
    in_degree = {node: 0 for node in nodes}

    # 1. Filter rules relevant to this sequence and build the graph
    for before, after in all_rules:
        if before in nodes and after in nodes:
            graph[before].append(after)
            in_degree[after] += 1

    # 2. Initialize a queue with all nodes that have no prerequisites
    queue = collections.deque([node for node in nodes if in_degree[node] == 0])
    sorted_list = []

    # 3. Process the queue
    while queue:
        current_node = queue.popleft()
        sorted_list.append(current_node)

        for neighbor in graph[current_node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # 4. If the sorted list contains all nodes, the sort was successful
    if len(sorted_list) == len(nodes):
        return sorted_list
    else:
        # A cycle was detected, so a valid ordering is impossible
        return None


def process_sequences(file_path: str):
    """
    Reads a file, validates sequences, calculates totals from valid and
    corrected rows, and attempts to reorder invalid ones.
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
        print("Error: Malformed input file.")
        return

    # --- Parse Rules ---
    rules = [tuple(map(int, line.strip().split('|'))) for line in rules_section.strip().split('\n') if '|' in line]
    print(f"--- Loaded {len(rules)} rules ---\n")

    # --- Process Sequences ---
    data_rows = data_section.strip().split('\n')

    # Initialize separate totals
    correct_total = 0
    corrected_total = 0

    for row_string in data_rows:
        sequence = [int(num) for num in row_string.strip().split(',')]
        is_valid = True

        # Validate the original sequence
        for before, after in rules:
            if before in sequence and after in sequence:
                if sequence.index(before) > sequence.index(after):
                    is_valid = False
                    break

        # --- Output and calculate totals based on validity ---
        if is_valid:
            print(f"✅ Valid:   {row_string}")
            middle_index = len(sequence) // 2
            correct_total += sequence[middle_index]
        else:
            # If invalid, attempt to reorder it
            corrected_sequence = topological_sort(sequence, rules)
            if corrected_sequence:
                corrected_str = ",".join(map(str, corrected_sequence))
                print(f"❌ Invalid: {row_string} -> Corrected: {corrected_str}")
                # Add the middle number of the *newly corrected* sequence to its own total
                middle_index = len(corrected_sequence) // 2
                corrected_total += corrected_sequence[middle_index]
            else:
                print(f"⛔ Invalid: {row_string} -> Correction failed (circular dependency)")

    # --- Print Final Totals ---
    overall_total = correct_total + corrected_total
    print("\n--- Calculation Complete ---")
    print(f"Sum of middle numbers from correct rows:     {correct_total}")
    print(f"Sum of middle numbers from corrected rows:   {corrected_total}")
    print("---------------------------------------------")
    print(f"Overall Total:                             {overall_total}")


# --- Main execution block ---
if __name__ == "__main__":
    INPUT_FILE = "input.txt"
    process_sequences(INPUT_FILE)