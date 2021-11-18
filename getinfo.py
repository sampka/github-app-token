import requests
import os

token = os.environ.get('TOKEN_ID')

url = "https://api.github.com/repos/sampka/AWS-EC2/branches/master/protection/required_signatures"

payload={}
headers = {
  'Authorization': 'Bearer ghs_PkcUBw1KVTZ0s0cELS3xW7IBkCKEoS4Ucffu'
}

response = requests.request("GET", url, headers=headers, data=payload)

text = response.text

print(response.text)

print(f"::set-output name=info::{text}")