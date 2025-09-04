# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests,os
from requests.auth import HTTPBasicAuth
import json

api_key = os.environ.get("API_KEY")
email = os.environ.get("EMAIL")

url = "https://kjithu2011.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth(email, api_key)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira issue created using python",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10003"
    },
    "project": {
      "key": "SCRUM"
    },
    "summary": "First issue created using python",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))