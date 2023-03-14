FROM python:alpine 

WORKDIR /work

COPY ./ /work/

RUN pip install -r requirements.txt

CMD ["python", "app/app.py"]