#!/usr/bin/env python
import subprocess

subprocess.call("ifconfig eth0 down", shell=True)
mac = input("Input mac address you want to change \(usaeg  aa:bb:cc:dd:ff:ee\):")
subprocess.call("ifconfig eth0 hw ether " + mac,shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
