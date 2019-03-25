
## What

Convert a http://www.floatrates.com/json-feeds.html daily rates json src file 
to valid Open Bank Project payload.

- Uses python3 

## Setup 

- You must have a valid Direct Login token
- You must have the `CanCreateFxRateAtAnyBank` permission

```
export ENDPOINT=<api.example.com>
export AUTH_TOKEN=<direct-login-token>
```

## Run
    pip install -r requirements.txt
    python3 convert.py

