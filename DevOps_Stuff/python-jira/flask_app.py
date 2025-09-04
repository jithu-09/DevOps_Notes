from flask import Flask # Importing Flask module from flask
import requests,os
from requests.auth import HTTPBasicAuth
import json

app=Flask(__name__) # Creating a Flask application instance
# The __name__ variable is a special built-in variable in Python that represents the name of the current module.

@app.route("/createJIRA", methods=['POST']) # This decorator defines the route for the function that follows it
#decorator performs an action(app route) before the function is called.
# Also gives the error message if route is not "/"
def createJIRA(): # Defining a function, served only at the root URL "/createJIRA"
    #api_key = os.environ.get("API_KEY")
    #email = os.environ.get("EMAIL")
    api_key="ATATT3xFfGF00-toJMs3n0OZpf8U501tkBrEuemlSm94QlWtrzKJxC6Gm39jK8YiYAov_Hh8NPF7JTkVHE8UWrJNu05JK1QyZhBEj5p8i4GSAPKfaBGZnaDkFUFJz2Xm85hrkMlmBigSZbyCy4rUhvHyCpWuD6Oitu3Ry98RioRyElffyLcizes=40474F93"
    email="k.jithu2011@gmail.com"

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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

app.run('0.0.0.0', port=5000) # This line runs the Flask application on all available IP addresses of the host machine
#in case of an ec2 instance, it will be accessible from the public IP address of the instance.
# The app.run() method starts the Flask application and makes it available to handle incoming requests.


