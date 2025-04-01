FROM ubuntu:latest

RUN apt update

RUN apt install -y python3 python3-pip python3-bs4 

WORKDIR /usr/src/app

COPY . .

RUN pip3  install --break-system-packages -r requirements.txt

RUN chmod +x main.py

CMD ["./main.py"]