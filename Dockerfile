FROM python:alpine

WORKDIR /app

COPY . /app/

RUN pip install Flask

CMD ["python", "app.py"]