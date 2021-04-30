FROM python:3.8-alpine

RUN apk update
RUN apk add python3-dev build-base linux-headers pcre-dev

RUN mkdir /code
WORKDIR /code
EXPOSE 5001

ADD . /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
