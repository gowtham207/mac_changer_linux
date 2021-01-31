import subprocess
import optparse


def user_input():
    parse_object=optparse.OptionParser()
    parse_object.add_option("-i","--interfacee",dest="interface",help="change to interface")
    parse_object.add_option("-m","--mac",dest="mac",help="to change mac address")
    return parse_object.parse_args()


def mac_change(iface,mac):
    subprocess.call(["ifconfig",iface,"down"])
    subprocess.call(["ifconfig",iface,"hw","ether",mac])
    subprocess.call(["ifconfig",iface,"up"])

print("      ***//The Mac Changer\\***")
print("-----------------------------------------")        
(i,a)=user_input()
mac_change(i.interface,i.mac)
print("completed")
