from os import environ, path
from dotenv import load_dotenv
from netmiko import ConnectHandler

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Executer:
    def __init__(self, device_ip):
        device = {
            'device_type': 'cisco_ios',
            'ip': device_ip,
            'username': environ.get('DEVICE_USERNAME'),
            'password': environ.get('DEVICE_PASSWORD')
        }
        self.connect = ConnectHandler(**device)

    def status(self, interface):
        output = self.connect.send_command(f'sh int {interface} des')
        return output

    def arp(self, interface):
        arp = self.connect.send_command(f'sh ip arp {interface}', use_textfsm=True)
        return arp

    def ping(self, ip):
        ping = self.connect.send_command(f'ping {ip}')
        return ping

    def disconnect(self):
        self.connect.disconnect()
