import sys

import requests

COMMAND_KEY = "command"
TARGET_URL_KEY = "target-url"
COMMENT_COMMAND_SUCCESS = "Command execution succeeded"
COMMENT_COMMAND_FAILURE = "Command execution failed"
COMMENT_COMMAND_BLANK = "Command is empty"
COMMENT_TARGET_URL_BLANK = "Target URL is blank"


class crawl_content:
    def check(self, action):
        return True

    def action(self, team_name, address, action, data):

        if TARGET_URL_KEY not in action:
            return False, COMMENT_TARGET_URL_BLANK, {}

        response = requests.get(action[TARGET_URL_KEY])
        if response.status_code == 200 and "Not Found (#404)" not in response.text:
            return True, COMMENT_COMMAND_SUCCESS, {}
        else:
            return False, COMMENT_COMMAND_FAILURE, {}
