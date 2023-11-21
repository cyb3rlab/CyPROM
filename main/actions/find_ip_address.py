import os
import subprocess
import socket
from datetime import date

COMMAND_KEY = "command"
TARGET_HOST_KEY = "host"
COMMENT_COMMAND_SUCCESS = "Command execution succeeded"
COMMENT_COMMAND_FAILURE = "Command execution failed"
COMMENT_COMMAND_BLANK = "Command is empty"
COMMENT_HOST_BLANK = "Target Host is empty"
CREATE_FILE_ERROR = "Fail to create file"


class find_ip_address:
    def check(self, action):
        # this action requires parameter "host"
        if TARGET_HOST_KEY in action:
            return True
        return False

    def action(self, team_name, address, action, data):
        if TARGET_HOST_KEY not in action:
            return False, COMMENT_HOST_BLANK, data
        else:
            # get the target host name
            target_host = action[TARGET_HOST_KEY]
            # get target host IP Address
            result = socket.gethostbyname(target_host)
            # if IP Address not found, return False
            if len(result) == 0:
                return False, COMMENT_COMMAND_FAILURE, {}
            else:
                return True, COMMENT_COMMAND_SUCCESS, result
