
## What this does

1. Fetch the json daily foreign exchange rates for each currency from http://www.floatrates.com/json-feeds.html.
2. Convert the json objects format to a the format supported by the Open Bank Project
3. Optionally POST them to an Open Bank Project instance using its api, or simply save the converted json to disk

### Requirements

- python3 

### Installation

```
# If you're on debian, you neede python3 and pip3
# e.g. apt install python3-pip
pip3 install fx2obp
```
###### Or, install directly from repo: 
```
git clone <this repo>
cd <this repo> 
pip install -e ./
```

## Configuration

- If you want to post to an Open Bank Project sandbox, you must:
  - have a valid Direct Login token: `AUTH_TOKEN`
  - specify the correct host to use : `API_HOST`
- You must have the `CanCreateFxRateAtAnyBank` permission

### Cron friendly

#### To install as a cronjob

1. Clone the repo
2. `cp update-fx-rates.py.example to update-fx-rates.py`
  2.1 Edit with your sandbox hostname and api token
3. Add a cron entry e.g. For everyday at 1am:
  3.1 `0 1 * * * /usr/bin/python3 /home/deploy/fx2obp/update-fx-rates.py >> /var/log/syslog`

Troubleshooting cron:

- Is python3 installed?
- Only use absolute paths, relative don't work in cron
- Can you run the command manually as that use, does it fail?


#### Run manually

###### Options

- WRITE_TO_FILE - Write output to disk
- POST_TO_OBP - Post to Open Bank Project api endpoint

**Note:** By default this wont post to the enpoint. This is to allow testing
to post to an endpoint, set the environment up:

```
export AUTH_TOKEN="direct-login-token"
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


