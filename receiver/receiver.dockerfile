FROM python:3.12-alpine

RUN apk add --no-cache curl

COPY . /receiver

RUN pip install -r /receiver/requirements.txt

EXPOSE 3000

CMD [ "uvicorn", "receiver.main:app", "--host", "0.0.0.0", "--port", "3000" , "--workers", "2"]
