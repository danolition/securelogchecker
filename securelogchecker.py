import re
filename = '/var/log/secure'
ips = []
for line in open(filename):
        match = re.search('^(.*?)\s(\w+)\ssshd.*?Failed\spassw.*?from\s(.*?)\sport.*$', line)
        if match:
                print match.groups()
        match = re.search('^(.*?)\s\w+\sssh.*?Invalid\suser\s(\w+)\sfrom\s(.*)', line)
        if match:
                print match.groups()
