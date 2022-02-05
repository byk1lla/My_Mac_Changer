import subprocess
import optparse

def get_user_input():
    parse_objesi = optparse.OptionParser()
    parse_objesi.add_option("-i","--interface",dest="interface",help="interface to change!")
    parse_objesi.add_option("-m","--mac",dest="mac_adress",help="New Mac Adress")
    return parse_objesi.parse_args()

def change_mac_adress(user_interface,user_mac_adress):
    subprocess.call(["sudo","ifconfig",user_interface,"down"])
    subprocess.call(["sudo","ifconfig",user_interface,"hw","ether",user_mac_adress])
    subprocess.call(["sudo","ifconfig",user_interface,"up"])
print("Mac Adresi Değiştirici")
(user_input,arguments)=get_user_input()
change_mac_adress(user_input.interface,user_input.mac_adress)