import sys

import requests

COMMAND_KEY = "command"
TARGET_URL_KEY = "target-url"
COMMENT_COMMAND_SUCCESS = "Command execution succeeded"
COMMENT_COMMAND_FAILURE = "Command execution failed"
COMMENT_COMMAND_BLANK = "Command is empty"
COMMENT_LOGIN_REQUIRED = "This action requires to login first"
COMMENT_LOGIN_FAILURE = "Login attemp failed"
COMMENT_LOGIN_DATA_BLANK = "Login data is empty"
COMMENT_TARGET_URL_BLANK = "Target URL is blank"


class crawl_content_auth:
    def check(self, action):
        return True

    def action(self, team_name, address, action, data):

        if len(data) < 1:
            return False, COMMENT_LOGIN_DATA_BLANK, {}

        if TARGET_URL_KEY not in action:
            return False, COMMENT_TARGET_URL_BLANK, {}

        # Create a session object
        session = requests.Session()

        # Send a POST request to the login endpoint
        response = session.get(data["login_url"], data=data["account"])

        # Check if the login was successful (you can customize this based on your Yii2 implementation)
        if response.status_code == 200:
            print("Login successful!")
        else:
            print("Login failed.")

        id = 1
        isStop = False
        while not isStop:
            # Now, you can send requests to the logged-in pages
            response = session.get(action[TARGET_URL_KEY] + str(id))
            if "Not Found (#404)" not in response.text:
                id += 1
            else:
                isStop = True

        if id > 1:
            return True, COMMENT_COMMAND_SUCCESS, data
        else:
            return False, COMMENT_COMMAND_FAILURE, data
