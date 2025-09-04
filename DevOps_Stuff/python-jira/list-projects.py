# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests,os
from requests.auth import HTTPBasicAuth
import json

api_key = os.environ.get("API_KEY")
email = os.environ.get("EMAIL")

url = "https://kjithu2011.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth(email, api_key)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

projectName= json.loads(response.text)
print(projectName[0]['name']) # [0] is used to get the first project name
