import time
import requests
import boto3
from requests_aws4auth import AWS4Auth

REGION = "eu-west-3" # <- à remplacer
URL = "https://epvxf8votc.execute-api.eu-west-1.amazonaws.com/load/test"  # <- à remplacer
SERVICE = "execute-api"

session = boto3.Session()
creds = session.get_credentials().get_frozen_credentials()
awsauth = AWS4Auth(creds.access_key, creds.secret_key, REGION, SERVICE, session_token=creds.token)

def burst(n=30, sleep_s=0.0):
    ok = 0
    throttled = 0
    other = 0
    for i in range(n):
        r = requests.get(URL, auth=awsauth, timeout=10)
        if r.status_code == 200:
            ok += 1
        elif r.status_code == 429:
            throttled += 1
        else:
            other += 1
        if sleep_s:
            time.sleep(sleep_s)
    return ok, throttled, other

if __name__ == "__main__":
    ok, th, other = burst(n=50, sleep_s=0.0)
    print(f"200={ok}  429={th}  other={other}")
