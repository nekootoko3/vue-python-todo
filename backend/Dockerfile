FROM python:3.8-buster

COPY . /app/
WORKDIR /app

RUN pip3 install -r requirements.lock

ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["./script/server"]
