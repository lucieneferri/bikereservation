FROM python:latest

WORKDIR /code/

RUN apt-get update
RUN apt-get install -y python3-dev default-libmysqlclient-dev netcat-traditional build-essential

COPY . .

RUN pip install -r requirements.txt 

EXPOSE 8000

CMD ["python3", "manage.py", "runserver"]