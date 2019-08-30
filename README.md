
## What this does

1. Fetch the json daily foreign exchange rates for each currency from http://www.floatrates.com/json-feeds.html.
2. Convert the json objects format to a the format supported by the Open Bank Project
3. Optionally POST them to an Open Bank Project instance using its api, or simply save the converted json to disk

### Requirements

- python3 

## Configuration

### Cron friendly

For cron example, see `update-fx-rates.py.example`

- If you want to post to an Open Bank Project sandbox, you must:
  - have a valid Direct Login token: `AUTH_TOKEN`
  - specify the correct host to use : `
- You must have the `CanCreateFxRateAtAnyBank` permission

```
export ENDPOINT=<api.example.com>
export AUTH_TOKEN=<direct-login-token>
```
#### Options

- WRITE_TO_FILE - Write output to disk
- POST_TO_OBP - Post to Open Bank Project api endpoint

**Note:** By default this wont post to the enpoint. This is to allow testing
to post to an endpoint, set the environment up:

```
export WRITE_TO_FILE=False
export POST_TO_OBP=True
```
The above allows you to test before blasting an endpint with invalid data.


## Run
    pip install -r requirements.txt
    python3 convert.py

