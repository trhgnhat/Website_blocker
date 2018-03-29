import time
from datetime import datetime as dt

#hosts_path=r"C:\\Windows\\System32\\drivers\\etc\\hosts"
#As same as *below*
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp="hosts"
redirect="127.0.0.1"
website_block_list = ["www.mail.live.com","https://outlook.live.com/owa/languageselection.aspx","https://outlook.live.com"]

print(dt.now().day)
while True:
    #Everyday from 8AM to 4PM, block the chosen websites.
    if dt(dt.now().year, dt.now().month, dt.now().day, 16) > dt.now() > dt(dt.now().year, dt.now().month, dt.now().day, 8):
        print("Working hours...")
        with open(hosts_path,"r+") as file:
            content = file.read()
            for website in website_block_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        print("Let's relax!!!")
        with open(hosts_path,"r+") as file:
            content = file.readlines()
            #move the pointer to the beginning of the file
            file.seek(0)
            #if every website in the web list NOT EXIST in a line, then write that line into hosts file.
            for line in content:
                if not any(website in line for website in website_block_list):
                    file.write(line)
            file.truncate()
            #delete the duplication.
    time.sleep(2)
