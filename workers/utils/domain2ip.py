import re
from socket import gethostbyname


def is_ip(string):
    p = re.compile("^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$")
    return True if p.match(string) else False


def convert(string):
    ip_list = string.split(",")
    index = 0
    for ip in ip_list:
        if not is_ip(ip):
            ip_list[index] = gethostbyname(ip)
        index += 1
    return ip_list
