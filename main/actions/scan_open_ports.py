import ipaddress
import nmap

COMMAND_KEY = "command"
TARGET_HOST_KEY = "host"
COMMENT_COMMAND_SUCCESS = "Command execution succeeded"
COMMENT_COMMAND_FAILURE = "Command execution failed"
COMMENT_COMMAND_BLANK = "Command is empty"
COMMENT_HOST_BLANK = "Target Host is empty"


class scan_open_ports:
    def check(self, action):
        return True

    def action(self, team_name, address, action, data):
        # create an instance of the Nmap PortScanner object
        nm = nmap.PortScanner()

        target_host = ""
        # specify the target host
        if TARGET_HOST_KEY in action:
            target_host = action[TARGET_HOST_KEY]
        else:
            return False, COMMENT_HOST_BLANK, {}

        if len(target_host) == 0:
            return False, COMMENT_HOST_BLANK, {}
        else:
            # perform a port scan on the target host which returns any ports with state = on
            nm.scan(hosts=target_host, arguments='-n -sV -Pn -A')

            result = []
            for host in nm.all_hosts():
                for proto in nm[host].all_protocols():
                    lport = nm[host][proto].keys()
                    # lport.sort()
                    for port in lport:
                        print("port: ", port)
                        result.append(port)
            if len(result) == 0:
                return False, COMMENT_COMMAND_FAILURE, {}
            else:
                return True, result, result
