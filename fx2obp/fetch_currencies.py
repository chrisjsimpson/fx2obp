from bs4 import BeautifulSoup
import requests
from time import sleep
from pathlib import Path
import tempfile

def fetch_currencies(ephemeral=False, **kwargs):
    """ Download every new foreign exchange rate available 
        
        :param ephemeral: Use a tempfs, don't persist to disk
                          as soon as all currencies have beed fetched, attempt
                          to post directly to an sandbox using postFx.
                          NOTE: this client code is also responsible for 
                          deleting the temporary directory and its contents 
                          when done with it as we use mkdtemp see
                          https://docs.python.org/3/library/tempfile.html
        :param sourceDir: As kwarg, may be used to override default folder
                          from which currencies are loaded (default is
                          './currencies' of the current working directory)
        :return: Path to currencies directory (either tmp or persistant)
    """

    html_doc = requests.get("http://www.floatrates.com/json-feeds.html")

    soup = BeautifulSoup(html_doc.text, "html.parser")

    download_links = []
    for link in soup.find_all("a"):
        try:
            if link["href"] and ".json" in link["href"]:
                download_links.append(link["href"])
        except:
            pass
    if ephemeral: # Prepare temp directory to store currencies & exchange rates
      path = tempfile.mkdtemp()
    else:
      try:
        path = kwargs['sourceDir']
      except KeyError:
        path = './currencies'

    # Download each currency conversion into list
    currencies = {}
    for target in download_links:
        try:
            # Get currency code
            currency_code = target.split("daily/")[1].split(".json")[0]
            resp = requests.get(target)
            currencies[currency_code] = resp.text
            print("Fetching {}".format(currency_code))
            # Write to file or tmpdir
            if ephemeral:
              filePath = Path(path, '{}.json'.format(currency_code))
            else: 
              filePath = Path("./currencies/{}.json".format(currency_code))
            with open(filePath, "w") as f:
                f.write(resp.text)
        except:
            raise
    return Path(path)


if __name__ == "__main__":
    fetch_currencies()
