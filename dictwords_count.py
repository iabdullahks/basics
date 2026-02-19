name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

# 1. Build the dictionary of counts
for line in handle:
    if not line.startswith("From "): 
        continue
    words = line.split()
    email = words[1]
    # Using the .get() method we just learned!
    counts[email] = counts.get(email, 0) + 1

# 2. Find the most prolific committer
bigcount = None
bigword = None

for word, count in counts.items():
    # If it's our first look (None) or if current count is larger
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
