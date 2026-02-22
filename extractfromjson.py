import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors (common when accessing https)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_2371982.json"

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

# Access the list of comments inside the 'comments' key
comments = js['comments']

total_sum = 0
count = 0

for item in comments:
    # Extract the 'count' value and convert to integer
    total_sum += int(item['count'])
    count += 1

print('Count:', count)
print('Sum:', total_sum)
