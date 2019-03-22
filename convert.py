import json

banks = ['bnpp-irb.04.pl.bgz', 'bnpp-irb.04.us.bow', 'bnpp-irb.04.tr.teb',
         'bnpp-irb.04.ua.ukrsibbank', 'bnpp-irb.04.ma.bmci', 
         'bnpp-irb.04.uk.uk']
currency_codes = ['chf', 'eur']

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
        output['from_currency_code'] = src_currency
        output['to_currency_code'] = to_currency
        output['conversion_value'] = currencies[to_currency]['rate']
        output['inverse_conversion_value'] = currencies[to_currency]['inverseRate']
        # For every bank, generate and write out the same exchange rate
        for bank in banks:
          output['bank_id'] = bank
          with open(bank + '-' + src_currency + '-' + to_currency + '-obp.json', 'w') as fp_output:
            fp_output.write(json.dumps(output))
  f.close()
