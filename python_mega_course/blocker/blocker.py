#!/usr/bin/env python3

import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
domain_list = [
    "www.facebook.com",
    "facebook.com",
    "mangarock.com",
    "www.sorozatbarat.online"
    ]


while True:
    year = dt.now().year
    month = dt.now().month
    day = dt.now().day
    if dt(year,month,day,9) < dt.now() and \
    dt.now() < dt(year,month,day,16):
    # I can use one comparison, but I prefer use "and"
        with open(hosts_path,"r+") as file:
            content = file.read()
            for domain in domain_list:
                if domain in content:
                    pass
                else:
                    file.write(redirect+" "+domain+"\n")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(domain in line for domain in domain_list):
                    file.write(line)
            file.truncate()
    time.sleep(5) #it's using seconds