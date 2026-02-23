import sqlite3

# 1. Connect to the database file mentioned in your assignment
conn = sqlite3.connect('org_counts.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

# 2. Update the table schema to use 'org' instead of 'email'
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    
    # 3. Extract the organization (domain) from the email
    # This splits 'stephen.marquard@uct.ac.za' into ['stephen.marquard', 'uct.ac.za']
    parts = email.split('@')
    org = parts[1]

    # 4. Update the SQL queries to use 'org'
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))

# 5. SPEED BOOST: Move conn.commit() out of the loop
# This writes to the disk once at the end instead of thousands of times.
conn.commit()

# Display the top 10 results
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print("Counts:")
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
