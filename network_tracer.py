import subprocess
import re
import requests

print('Write the host name or ip:')
host = str(input())
qest = 'traceroute ' + host
reqest = subprocess.getoutput(qest)
way = re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}.[0-9]{1,3}', reqest)

way = re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}.[0-9]{1,3}', (subprocess.getoutput('traceroute ' + str(input()))))

#way_for_ya = ['87.250.250.242',
            # '10.97.191.254',
#             '10.97.191.254',
#             '10.255.201.6',
#             '10.255.201.6',
#             '10.255.101.5',
#             '10.255.101.5',
#             '10.255.100.2',
#             '10.255.100.2',
#             '194.85.107.57',
#             '87.250.239.17',
#             '10.1.2.2',
#             '10.1.2.2']

for ip in way_for_ya:
    answer = requests.get('https://ipinfo.io/' + ip + '/json').text
    print(answer)
    answer = ''
