import requests
import os

url = "https://api.github.com/repos/sampka/AWS-EC2/branches/master/protection/required_signatures"

payload={}
headers = {
  'Authorization': 'Bearer ghs_yWRc3pjaiezqxhkun0MhOGXBn5wXHq46Uiy0'
}

response = requests.request("GET", url, headers=headers, data=payload)

text = response.text

print(response.text)

print(f"::set-output name=info::{text}")