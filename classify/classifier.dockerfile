FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y \
    libgtk2.0-dev\
    pkg-config\
    libavformat-dev\
    libtbb-dev\
    libdcmtk-dev\
    libjpeg-dev\
    libpng-dev\
    libtiff-dev &&\
    rm -rf /var/lib/apt/list/*

COPY requirements.txt .
COPY ./app ./app
RUN pip install -r requirements.txt

EXPOSE 4000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0","--port", "4000" , "--workers","2"]
