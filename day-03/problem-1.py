import re

# It only finds `mul(X,Y)`
regex_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

total_sum = 0

try:
    with open('input.txt', 'r') as file:
        content = file.read()

    # Find all occurrences that match the pattern
    matches = re.findall(regex_pattern, content)

    for match in matches:
        num1 = int(match[0])
        num2 = int(match[1])
        result = num1 * num2
        total_sum += result

        print(f"Found: mul({num1},{num2}) -> Result: {result}")

    print("\n------------------------------------------")
    print(f"✅ Final Total Sum: {total_sum}")

except FileNotFoundError:
    print(f"Error: The file was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")