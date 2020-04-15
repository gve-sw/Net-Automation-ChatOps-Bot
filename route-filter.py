'''from netmiko import ConnectHandler
from getpass import getpass
node = {
    "host": "ipaddr",
    "username": "ansible",
    #"password": getpass(),
    "password": "ansible123",
    "device_type": "cisco_ios",
}
net_connect = ConnectHandler(**node)
output = net_connect.send_command("show ip route dest")
print(output)
net_connect.disconnect()'''

print("\nshow ip route dest command executed.")
print("\nSubnet not in table.")