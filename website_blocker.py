from datetime import datetime as dt
import time

hosts_path = "/etc/hosts"
# hosts_path = r"C:\Windows\System32\drivers\etc\hosts" -----> in Windows

redirect = "127.0.0.1"

# list of websites to be blocked
website_list = ["www.facebook.com", "facebook.com"]

while True:
    # replace 8 and 16 with your start and end time in 24H format
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() <  dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n" + redirect + " " + website)
    else:
        print("Enjoy browsing :)")
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    # the script runs every 5 mins (300 = 5 x 60 secs)
    time.sleep(300)
