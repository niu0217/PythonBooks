#! python3
# searchpypi.py
# Opens serveral search results.
import sys

import requests
import webbrowser
import bs4
import pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    address = '+'.join(sys.argv[1:])
else:
    # Get address from clipboard
    pastelist = pyperclip.paste().split()
    address = '+'.join(pastelist)

print('Searching...')
res = requests.get('https://pypi.org/search/?q=' + address)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('.package-snippet')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org/search/?q=' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
