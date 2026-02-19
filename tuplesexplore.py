name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    # 1. Filter for the 'From ' lines
    if not line.startswith("From "):
        continue
    
    # 2. Split the line into words
    words = line.split()
    
    # 3. The time is the 5th index (09:14:16)
    time = words[5]
    
    # 4. Split the time string by the colon to get the hour
    # ['09', '14', '16'] -> Index 0 is the hour
    hour = time.split(':')[0]
    
    # 5. Tally the hour in the dictionary
    counts[hour] = counts.get(hour, 0) + 1

# 6. Sort the dictionary by keys (hours)
# We can use sorted() directly on counts.items()
for key, val in sorted(counts.items()):
    print(key, val)
