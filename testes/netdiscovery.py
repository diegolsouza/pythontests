#!/usr/bin/env python3
#from __future__ import absolute_import, division, print_function
#from getpass import getpass
from sys import exit, argv
#import paramiko
#import netmiko
#import pprint
#import json
#import signal
#import pyping
import os
#signal.signal(signal.SIGPIPE.signal.SIG_DFL)
#signal.signal(signal.SIGINT.signal.SIG_DFL)

USE_IP_RANGE = True
IP_RANGE = ['10.2.0.100', '10.2.0.135']
#NETWORKS = ['10.10.0.0/23', '10.11.8.0/23',]
#PORT = 22

#def enumerate_ips():
iplist = []
start = list(map(int, IP_RANGE[0].split(".")))
end = list(map(int, IP_RANGE[1].split(".")))
temp = start
iplist.append(IP_RANGE[0])
while temp != end:
    start[3] += 1
    for i in (3, 2, 1):
        if temp[i] == 256:
            temp[i] = 0
            temp[i-1] += 1
#            print(os.system("ping -c 1 " + ip)
    ipadd=(".".join(map(str, temp)))
    iplist.append(ipadd)
    response = os.system("ping -c 1 " + ipadd)
    if response == 0:
        print(ipadd, 'is up!')
    else:
        print(ipadd, 'is down!')
    #print(ipadd)
