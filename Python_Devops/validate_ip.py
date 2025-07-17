import re

ip ="198.168.1.1"
pattern = r'^(\d{1,3}\.){3}\d{1,3}$'

if re.match(pattern,ip):
    print("valid ip address")
else:
    print("invalid")