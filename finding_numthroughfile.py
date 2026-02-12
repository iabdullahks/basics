# Use mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

total_value = 0.0
count = 0

for line in fh:
    # Skip lines that don't start with the target string
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    
    # 1. Find the colon
    pos = line.find(':')
    
    # 2. Extract the number (jump +1 past the colon and strip spaces)
    number_str = line[pos + 1:].strip()
    
    # 3. Convert to float and update our accumulators
    value = float(number_str)
    total_value = total_value + value
    count = count + 1

# Calculate the average after the loop finishes
if count > 0:
    average = total_value / count
    print("Average spam confidence:", average)
else:
    print("No lines found.")
