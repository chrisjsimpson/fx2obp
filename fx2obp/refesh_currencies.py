from bs4 import BeautifulSoup
import requests
from time import sleep
from pathlib import Path

html_doc = requests.get("http://www.floatrates.com/json-feeds.html")

soup = BeautifulSoup(html_doc.text, 'html.parser')

def refesh_currencies():
  download_links = []
  for link in soup.find_all('a'):
    try:
      if link['href'] and '.json' in link['href']:
        download_links.append(link['href'])
    except:
      pass
  # Download each currency conversion into list
  currencies = {}
  for target in download_links:
    try:
      # Get currency code
      currency_code = target.split('daily/')[1].split('.json')[0]
      resp = requests.get(target)
      currencies[currency_code] = resp.text
      print("Added {}".format(currency_code))
      # Write to file
      p = Path('./currencies/{}.json'.format(currency_code))
      with open(p, 'w') as f:
        f.write(resp.text)
    except:
      raise
  return currencies

refesh_currencies()
