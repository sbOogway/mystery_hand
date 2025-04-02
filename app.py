#!/usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup
import os
from flask import  Flask, render_template, request, redirect
from urllib.parse import urlparse, parse_qs
import logging


app = Flask(__name__)
app.logger.setLevel(logging.INFO)
p = re.compile(r'"videoId":"(.*?)"')
p2 = re.compile(r'data-ph-capture-attribute-title="(.*?)"')

@app.route('/', methods=["GET"])
def render_home():
    files = sorted(os.listdir("hands"))
    # print(files)    
    app.logger.info(f"handled get home")
    return render_template("index.html", files=files)

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        link = parse_qs(urlparse(request.form["yt"]).query)["v"][0]
        print(link)
        app.logger.info(f"handled {link}")
        get_mistery(link)
    app.logger.info(f"handled post submit")
    return redirect("/", code=302)

@app.route("/<path:file>")
def serve(file):
    if file == "favicon.ico":
        return ''
    with open(f"hands/{file}", "r") as f:
        c = f.readlines()
    c = [e.strip() for e in c]
    app.logger.info(f"handled {file}")
    return render_template("hands.html", links=c)


def get_mistery(link):
    transcript = requests.get(f"https://youtubetotranscript.com/transcript?v={link}&current_language_code=en").content.decode()

    video_title = p2.findall(transcript)[0].replace("#", "").replace("&", "").replace(",", "").replace(" ", "_").replace("|", "").replace("$", "").replace(";", "").replace(":", "").replace("'", "").replace("\"", "")

    print(video_title) 
    if "🔴" in video_title:
        return
    
    soup = BeautifulSoup(transcript, 'html.parser')

    try:
        transcript = soup.find(id='transcript').find('p').find_all('span')
    except AttributeError:
        return

    for e in transcript:
        if "mystery hand" in str(e):
            # print(e['data-start'])
            # print(e.text)
            t = e['data-start'].split('.')[0]
            # print(f"https://youtube.com/watch?v={link}&t={t}")
            os.system(f"touch hands/{video_title}")
            os.system(f'grep -qxF "https://youtube.com/watch?v={link}\&t={t}" hands/{video_title} || echo "https://youtube.com/watch?v={link}\&t={t}" >> hands/{video_title} ')
            # print("-" * 50)





if __name__ == "__main__":

    # data = requests.get("https://www.youtube.com/@TritonPoker/streams").content.decode()

    # # print(data)

    # links = p.findall(data)
    # links = list(set(links))

    # for link in links:
    #     get_mistery(link)
    app.run(debug=False, port=7777)
