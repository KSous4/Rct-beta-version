FROM python:3.12-alpine

COPY . /exit

WORKDIR /exit

RUN pip install -r /entrance/requirements.txt

CMD [ "python3", "main.py"]