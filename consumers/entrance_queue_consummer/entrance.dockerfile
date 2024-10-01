FROM python:3.12-alpine

COPY . /entrance

WORKDIR /entrance

RUN pip install -r /entrance/requirements.txt

CMD [ "python3", "main.py"]
