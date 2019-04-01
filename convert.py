import json
import requests
import os
from datetime import datetime

POST_TO_OBP=os.getenv('POST_TO_OBP', '')
WRITE_TO_FILE=os.getenv('WRITE_TO_FILE', '')
ENDPOINT = os.getenv('ENDPOINT')
POST_URL="{}/obp/v3.1.0/banks/{}/fx"
AUTH_TOKEN=os.getenv('AUTH_TOKEN')

# Get bank ids
url = 'https://bnpparibas-irb.openbankproject.com/obp/v3.1.0/banks'
req = requests.get(url, headers={'Content-Type':'Application/Json'})
banks = json.loads(req.text)['banks']

currency_codes = ['dzd', 'gbp', 'chf', 'eur']

'''
For each file input , convert it to an OBP foriegn exchange valid payload.
Populate for each bank.

Required roles:
- CanCreateFxRate
- CanCreateFxRateAtAnyBank

Valid example:
{
  "bank_id":"bankid123",
  "from_currency_code":"EUR",
  "to_currency_code":"USD",
  "conversion_value":1.0,
  "inverse_conversion_value":1.0,
  "effective_date":"2017-09-19T00:00:00Z"
}
Invalid format example from source: (http://www.floatrates.com)
"usd": {
  "code": "USD",
  "alphaCode": "USD",
  "numericCode": "840",
  "name": "U.S. Dollar",
  "rate": 1.0001337101383,
  "date": "Wed, 20 Mar 2019 12:00:02 GMT",
  "inverseRate": 0.9998663077377
}
'''
for src_currency in currency_codes:
  with open(src_currency + '.json') as f:
      data = f.read()
      currencies = json.loads(data) 
      for to_currency in currencies:
        output = {}
        output['from_currency_code'] = str(src_currency.upper())
        output['to_currency_code'] = str(to_currency.upper())
        output['conversion_value'] = currencies[to_currency]['rate']
        output['inverse_conversion_value'] = currencies[to_currency]['inverseRate']
        src_date = currencies[to_currency]['date']
        src_date_format = "%a, %d %b %Y %H:%M:%S %Z"
        date = datetime.strptime(src_date, src_date_format)
        dst_date_format = "%Y-%m-%dT%k:%M:%S%ZZ"
        output['effective_date'] = date.strftime(dst_date_format)
        # For every bank, generate and write out the same exchange rate
        for bank in banks:
          output['bank_id'] = bank['id']
          if POST_TO_OBP.lower() == 'true':
            url = POST_URL.format(ENDPOINT, bank['id'])
            print(url)
            print (output)
            authorization = 'DirectLogin token="{}"'.format(AUTH_TOKEN)
            headers = {'Content-Type': 'application/json',
                      'Authorization': authorization}
            request = requests.put(url, headers=headers, data=json.dumps(output))
            print(request.text)
          if WRITE_TO_FILE.lower() == 'true':
            with open(bank['id'] + '-' + src_currency + '-' + to_currency + '-obp.json', 'w') as fp_output:
                fp_output.write(json.dumps(output))
  f.close()
