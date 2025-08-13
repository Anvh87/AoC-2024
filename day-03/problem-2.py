import re

# Find the exact substrings 'mul(x,y)', 'do()', or 'don't()'
regex_pattern = r"(?P<MUL>mul\((\d{1,3}),(\d{1,3})\))|(?P<DO>do\(\))|(?P<DONT>don't\(\))"

# --- State Variables ---
is_mul_enabled = True  # Start with mul enabled
total_sum = 0

try:
    with open('input.txt', 'r') as file:
        content = file.read()

    # We use re.finditer to find all matches in the order they appear
    for match in re.finditer(regex_pattern, content):

        if match.group('MUL'):
            # Found a mul() command
            num1_str, num2_str = match.group(2), match.group(3)
            if is_mul_enabled:
                num1, num2 = int(num1_str), int(num2_str)
                result = num1 * num2
                total_sum += result
                print(f"✅ mul({num1},{num2}) processed. Result: {result}. New Sum: {total_sum}")
            else:
                print(f"❌ mul({num1_str},{num2_str}) skipped (processing is disabled).")

        elif match.group('DO'):
            # The exact substring 'do()' was found
            is_mul_enabled = True
            print(f"🟢 Substring 'do()' found. mul() is now ENABLED.")

        elif match.group('DONT'):
            # The exact substring 'don't()' was found
            is_mul_enabled = False
            print(f"🔴 Substring 'don't()' found. mul() is now DISABLED.")

    print("\n----------------------------------------------------")
    print(f"✅ Final Total Sum: {total_sum}")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")