import requests 
import re
import app
import os

if __name__ == "__main__":
    data = requests.get("https://www.youtube.com/@TritonPoker/streams").content.decode()

    # print(data)

    links = app.p.findall(data)
    links = list(set(links))

    print(links)
    for link in links:
        # app.get_mistery(link)
        # os.system()

        url = "http://debian-srv:7777/submit"

        payload = f"yt=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D{link}%26t%3D27s"
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "http://debian-srv:7777",
            "Connection": "keep-alive",
            "Referer": "http://debian-srv:7777/",
            "Cookie": "_pk_id.1.da80=a11f4d68f0389696.1723566863.; wp-settings-time-1=1724768918; wp-settings-1=libraryContent%3Dupload",
            "Upgrade-Insecure-Requests": "1",
            "Priority": "u=0, i",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response)
        # r = requests.post("http://debian-srv:7777/submit", data={"yt":"https://www.youtube.com/watch?v={link}&t=24s"})
        # print(r)