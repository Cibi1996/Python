#!/bin/usr/env python
import subprocess
import optparse
import re
def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its Mac_Address")
    parser.add_option("-m", "--mac", dest="new_mac_address", help="New Mac_Address")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please enter interface.Use help for more info")
    elif not options.new_mac_address:
        parser.error("[-] Please enter mac.Use help for more info")
    return options

def mac_change(interface,new_mac_address):
    print("[+] Changing Mac Address For " + interface + " to " + new_mac_address)
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_address])
    subprocess.call(["ifconfig", interface, "down"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    macaddress_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if macaddress_search_result:
        return macaddress_search_result.group(0)
    else:
        print("[-] Could Not Read Mac Address")


options = get_args()
current_macaddress=get_current_mac(options.interface)
print("Current Mac = "+str(current_macaddress))
mac_change(options.interface,options.new_mac_address)

current_mac=get_current_mac(options.interface)
if current_mac == options.new_mac_address:
    print("[+] MAC Address was successfully changed to" + current_mac)
else:
    print("[-] MAC Address did not get changed")






