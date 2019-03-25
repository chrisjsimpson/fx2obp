
## What

- Convert a http://www.floatrates.com/json-feeds.html daily rates json src file 
to valid Open Bank Project payload.
- HTTP PUT them to an Open Bank Project endpoint to populate the database via the `fx` api call

- Uses python3 

## Setup 

- You must have a valid Direct Login token
- You must have the `CanCreateFxRateAtAnyBank` permission

```
export ENDPOINT=<api.example.com>
export AUTH_TOKEN=<direct-login-token>
```
#### Options

- WRITE_TO_FILE - Write output to disk
- POST_TO_OBP - Post to Open Bank Project api endpoint

```
export WRITE_TO_FILE=False
export POST_TO_OBP=True
```


## Run
    pip install -r requirements.txt
    python3 convert.py

