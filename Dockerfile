FROM python:3.8-slim-buster

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --root-user-action=ignore --upgrade wheel setuptools pip && pip install --root-user-action=ignore -r requirements.txt

COPY . /app

ENV FLASK_APP=main.py

EXPOSE 5000

CMD python3 -m flask run  --host="0.0.0.0"
