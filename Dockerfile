FROM python:3.10-alpine

WORKDIR usr/alzheimer-app/

COPY . .

RUN pip install -r requirements.txt

CMD python3 main.py