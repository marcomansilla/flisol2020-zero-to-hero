FROM python:3.6-alpine

COPY ./app/* /app/

WORKDIR /app

RUN pip3 install -r requirements.txt

WORKDIR /app

CMD ["python", "app.py"]
