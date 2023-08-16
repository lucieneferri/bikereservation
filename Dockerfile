FROM python:latest

WORKDIR /code/

COPY . .

RUN pip install -r requirements.txt 

EXPOSE 8000

CMD ["python3", "manage.py", "runserver"]