import requests
import os
import bs4


url = 'http://xkcd.com'                 # starting url
os.makedirs('xkcd', exist_ok=True)      # store comics in ./xkcd

url = 'http://xkcd.com'
os.makedirs('xkcd2', exist_ok=True)
while not url.endswith('#')
print('Downloading pag %s...' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
