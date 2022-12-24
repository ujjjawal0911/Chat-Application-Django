FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1 
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN apt update && apt upgrade -y
RUN pip install --upgrade pip

COPY . .
RUN pip install -r requirements.txt

EXPOSE 8000
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]