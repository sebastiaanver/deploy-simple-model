FROM python:3.7

WORKDIR /usr/src/app
COPY . .

RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "./app.py"]
