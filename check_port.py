#!/usr/bin/env python
# rhn_checker.py
# For testing communication to Red Hat Network and Red Hat Subscription Manager services
# when netcat and telnet are unavailable.
# Authored by Robb Manes <rmanes@redhat.com>
# Modified by Scott Parker

import sys
import socket

def check_port( satellite, service, port ):
  try:
     error = 0
     httpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     httpSock.settimeout(20)
     httpSock.connect(( satellite, port ))
     httpSock.settimeout(None)
     httpSock.close()
     print("\tSuccessful connection on port {0} ({1}) to {2}.".format(port,service,satellite))
  except socket.error, (value, message):
     if httpSock:
        httpSock.close()
        print("\tFAILED!! Connection on server port {1} ({1}) to {2} failed!!".format(port,service,satellite))
        error += 1

# main

# Ports and Descriptions
ports = (
('HTTP', 80),
('SSL', 443),
('Subscription Management Services', 8443),
('Katello Agent', 5647),
('OpenSCAP', 9090),
('Anaconda Kickstart', 8000),
('Puppet Agent',8140),
('OpenSCAP Reports',9090),
('DNS',53),
('DHCP Broadcast',67),
('PXE Boot',69)
)

satellite = str(sys.argv[1])
for (service, port) in ports:
   check_port( satellite, service, port )
