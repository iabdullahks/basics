import re

# Use your specific file name here
filename = "actual_data.txt"

try:
    with open(filename, 'r') as file:
        total_sum = 0
        count = 0
        
        for line in file:
            # Find all sequences of numbers in the line
            numbers = re.findall('[0-9]+', line)
            
            # If no numbers found, skip to the next line
            if not numbers:
                continue
                
            # Convert string matches to integers and add to total
            for num in numbers:
                total_sum += int(num)
                count += 1
        
        print(f"Total count of values: {count}")
        print(f"Final Sum: {total_sum}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
