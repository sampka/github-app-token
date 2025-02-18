#!/usr/bin/env python3

import time
import requests
import jwt
import os
import json


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = f"Bearer {self.token}"
        print(r.headers["authorization"])
        return r

if __name__ == '__main__':

    app_id = os.environ.get('INPUT_APP_ID')
    app_installation_id = os.environ.get('INPUT_APP_INSTALLATION_ID')
    app_key = os.environ.get('INPUT_APP_PEM')

    time_since_epoch_in_seconds = int(time.time())
    payload = {
        # issued at time
        "iat": time_since_epoch_in_seconds,
        # JWT expiration time (10 minute maximum)
        "exp": time_since_epoch_in_seconds + (10 * 60) - 10,
        # GitHub App's identifier
        "iss": app_id,
    }

    encoded_jwt = jwt.encode(payload, app_key, algorithm="RS256")

    call_headers = {"Accept": "application/vnd.github.machine-man-preview+json"}

    get_installation_token_url = (
        f"https://api.github.com/app/installations/{app_installation_id}/access_tokens"
    )
    get_installation_token_response = requests.post(
        get_installation_token_url,
        headers=call_headers,
        auth=BearerAuth(encoded_jwt),
    )

    token = get_installation_token_response.json()["token"]

    print(f"::add-mask::{token}")
    print(f"::set-output name=app_token::{token}")

    #Check for GPG Commit Signing


    url = "https://api.github.com/users/sampka/repos"

    headers = {
      'Content-Type': 'application/json',
      'Authorization': f"Bearer {token}"
    }


    payload = json.dumps({
    "subscribed": "true"
    })


    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text.name)





    url = "https://api.github.com/repos/sampka/AWS-EC2/branches/master/protection/required_signatures"

    payload={}

    response = requests.request("GET", url, headers=headers, data=payload)

    text = response.text

    print(response.text)

    print(f"::set-output name=info::{text}")
