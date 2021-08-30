t('''example: xPathgrabber.py {URL} {XPATH} {--hidden for 'hidden' content}\n\n''')

from lxml import html
import requests
import sys

xpathcode = sys.argv[2]
url = sys.argv[1]

# error correction
try:
	mode = sys.argv[3]
except:
	mode = None

# mode
if xpathcode[-1] != ")" and mode == "--hidden":
	xpathcode = xpathcode+"//text()"

if xpathcode[-1] != ")":
	xpathcode = xpathcode+"/text()"

# logic
r = requests.get(f'{url}')
tree = html.fromstring(r.content)
output = tree.xpath(f'''{xpathcode}''')

print(output)