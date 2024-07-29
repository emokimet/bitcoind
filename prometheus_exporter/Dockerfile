FROM python:3.9.13-alpine
RUN mkdir /code
WORKDIR /code
EXPOSE 8000

RUN apk update && apk add --no-cache gcc musl-dev linux-headers

ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD app.py /code/

CMD ["python", "app.py"]
