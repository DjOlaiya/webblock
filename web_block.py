#website blocker app.
#script should be run as root
import time
import tkinter as tk
from datetime import datetime as dt

#host path is OS specific
hosts_path= "/etc/hosts"
#local IP
#redirect= "185.199.108.153"
redirect="127.0.0.1"

#website to block
website_list= []
#["netflix.com","www.netflix.com","youtube.com","www.youtube.com"]

printlist=["Let's get down to business","to defeat the Huns", "Did they send me daughters", "when I asked for sons",
"you're a spineless pale pathetic lot", "but you can bet before I'm through", "somehow I'll get an A out of you"]
num=0
while True:
 #my busy period. rewrite this to something more realistic take it in as an input
    i = (num) % 7
    if dt(dt.now().year,dt.now().month,dt.now().day,15,55) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,15,57):

        print(printlist[i])

        with open(hosts_path, "r+") as file:
            content=file.readlines()
            file.seek(0)

            for website in website_list:
#if statement passes if website is already in list
                if website in content:
                    pass
                else:
                #else it adds to list and blocks new address
                #map hostnames to blocked IP
                    file.write(redirect + " " + website + "\n")

    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            #remove from block list
            file.truncate()
        print("free time")
    num += 1
    time.sleep(2)


