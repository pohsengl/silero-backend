FROM python:3.8.13-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /djangoapp
COPY requirements.txt /djangoapp/
RUN pip install -r requirements.txt
COPY . /djangoapp/