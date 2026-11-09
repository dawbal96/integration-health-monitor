# Integration Health Monitor

A small Python tool that checks whether a list of APIs is up, records how each one responded, and writes the results to a log file. I'm building it step by step to strengthen my Python and Linux skills for technical support roles.

## Why I built this

In my last product support role, I looked after integration monitors for AWS, Azure and GCP. A big part of the job was reading logs to work out why an integration had failed, and many failures turned out to be timeouts caused by temporary network issues rather than real problems. This project rebuilds that kind of monitoring from scratch, so I understand every part of it, from the API call to the log line.

## What it does

- Checks a list of APIs over HTTPS
- Records the status code and response time for each check
- Marks each check as SUCCESS or FAILURE
- Tells apart three kinds of failure: a bad status code (for example 404), a timeout, and a connection error (for example a DNS failure)
- Keeps going when one API fails, so one broken check doesn't stop the rest
- Writes a timestamped line for every check to `monitor.log`

## Example log output

```
2026-11-09 16:13:11,178 INFO url=https://api.github.com status=200 time=0.164925 result=SUCCESS
2026-11-09 16:13:11,183 ERROR url=https://this-domain-does-not-exist.invalid result=FAILURE error=ConnectionError
2026-11-09 16:13:11,425 ERROR url=https://api.github.com/this-does-not-exist status=404 time=0.241336 result=FAILURE
```

Every line uses the same `key=value` format, so the log is easy to search:

```
grep ERROR monitor.log        # show every failure
grep -c ERROR monitor.log     # count them
```

## How to run it

Requires Python 3 on Linux (developed on Ubuntu under WSL).

```
git clone https://github.com/dawbal96/integration-health-monitor.git
cd integration-health-monitor
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python check_api.py
```

Results are printed to the screen and added to `monitor.log`.

## Test cases

Two of the URLs in the list are meant to fail:

- `https://this-domain-does-not-exist.invalid` uses the `.invalid` domain, which is reserved and never exists, to show how a connection error is handled.
- `https://api.github.com/this-does-not-exist` returns a 404, to show how a bad status code is handled.

## Status

In progress. Planned next:

- Run the checks automatically on a schedule with cron
- A second script that analyses the log: failure counts, error types, and whether failures look temporary or need investigating
- A runbook for support engineers: how to investigate with `grep` and `tail`, and when to retry vs escalate
