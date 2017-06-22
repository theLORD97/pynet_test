"""
pynet-rtr1 (Cisco IOS)  184.105.247.70
pynet-rtr2 (Cisco IOS)  184.105.247.71
pynet-sw1  (Arista EOS) 184.105.247.72
pynet-sw2  (Arista EOS) 184.105.247.73
pynet-sw3  (Arista EOS) 184.105.247.74
pynet-sw4  (Arista EOS) 184.105.247.75
juniper-srx             184.105.247.76
"""
from getpass import getpass

std_pwd = getpass("Enter standard password: ")

pynet_rtr1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': std_pwd,
}

pynet_rtr2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': std_pwd,
}

pynet_sw1 = {
    'device_type': 'arista_eos',
    'ip': '184.105.247.72',
    'username': 'pyclass',
    'password': std_pwd,
}

pynet_sw2 = {
    'device_type': 'arista_eos',
    'ip': '184.105.247.73',
    'username': 'pyclass',
    'password': std_pwd,
}

pynet_sw3 = {
    'device_type': 'arista_eos',
    'ip': '184.105.247.74',
    'username': 'pyclass',
    'password': std_pwd,
}

pynet_sw4 = {
    'device_type': 'arista_eos',
    'ip': '184.105.247.75',
    'username': 'pyclass',
    'password': std_pwd,
}

juniper_srx = {
    'device_type': 'juniper_junos',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'password': std_pwd,
}

passwd = std_pwd
juniper1 = { 
        "host": "juniper1.twb-tech.com",
        "user": "pyclass",
        "password": passwd,
}   

juniper2 = { 
        "host": "juniper2.twb-tech.com",
        "user": "pyclass",
        "password": passwd,
}
   
juniper3 = { 
        "host": "juniper3.twb-tech.com",
        "user": "pyclass",
        "password": passwd,
}
   
juniper4 = { 
        "host": "juniper4.twb-tech.com",
        "user": "pyclass",
        "password": passwd,
}


device_list = [
        pynet_rtr1,
        pynet_rtr2,
        pynet_sw1,
        pynet_sw2,
        pynet_sw3,
        pynet_sw4,
        juniper_srx,
]

juniper_vmx = [
        juniper1,
        juniper2,
        juniper3,
        juniper4,
]



