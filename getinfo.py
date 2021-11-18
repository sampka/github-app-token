import requests
import os

token = os.environ.get('TOKEN_ID')

print(token)
#print(len(token))


url = "https://api.github.com/repos/sampka/AWS-EC2/branches/master/protection/required_signatures"

payload={}
headers = {
  'Authorization': 'Bearer {token}'
}

response = requests.request("GET", url, headers=headers, data=payload)

text = response.text

print(response.text)

print(f"::set-output name=info::{text}")