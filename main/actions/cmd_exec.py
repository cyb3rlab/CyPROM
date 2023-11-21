import fileinput
import re
import subprocess

COMMAND_KEY = "command"
COMMENT_COMMAND_SUCCESS = "Command execution succeeded"
COMMENT_COMMAND_FAILURE = "Command execution failed"
COMMENT_COMMAND_BLANK = "Command is empty"


class cmd_exec:
    def check(self, action):
        # All parameters are optional, so no checking done
        return True

    def action(self, team_name, address, action, data):
        if COMMAND_KEY not in action:
            return False, COMMENT_COMMAND_BLANK, {}
        else:
            for command in action[COMMAND_KEY]:
                # replace the args @team_name with the team_name from target file
                command = re.sub("@team_name", team_name, command)
                # exec the command
                command_exec = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE, universal_newlines=True)
                output, error = command_exec.communicate()

                countOutputLine = 0
                countErrorLine = 0
                for line in output:
                    countOutputLine += 1
                for line in error:
                    print(line)
                    countErrorLine += 1

                if countOutputLine == 0 and countErrorLine != 0:
                    return False, COMMENT_COMMAND_FAILURE, {}

        return True, COMMENT_COMMAND_SUCCESS, output
