FROM python:3.6.1-alpine
RUN mkdir /code
WORKDIR /code
EXPOSE 8000

ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD app.py /code/

CMD ["python", "app.py"]
