
## What this does

1. Fetch the json daily foreign exchange rates for each currency from http://www.floatrates.com/json-feeds.html.
2. Convert the json objects format to a the format supported by the Open Bank Project
3. Optionally POST them to an Open Bank Project instance using its api, or simply save the converted json to disk

### Requirements

- python3 

## Configuration

### Cron friendly

#### To install as a cronjob
```
For cron example, see `update-fx-rates.py.example`

- If you want to post to an Open Bank Project sandbox, you must:
  - have a valid Direct Login token: `AUTH_TOKEN`
  - specify the correct host to use : `
- You must have the `CanCreateFxRateAtAnyBank` permission

#### Run manually

###### Options

- WRITE_TO_FILE - Write output to disk
- POST_TO_OBP - Post to Open Bank Project api endpoint

**Note:** By default this wont post to the enpoint. This is to allow testing
to post to an endpoint, set the environment up:

```
export AUTH_TOKEN=<direct-login-token>
export WRITE_TO_FILE=False
export POST_TO_OBP=True
```
The `WRITE_TO_FILE` and `POST_TO_OBP` allows you to test before 
blasting an endpint with invalid data.

Set options, then run 

```
python3 convert.py
```
You will then see the script first download the latest exchange rates, 
and then post them to the Open Bank Project instance if specified.




## Run
    pip install -r requirements.txt
    python3 convert.py

