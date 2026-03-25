FROM python:3.10

WORKDIR /app

COPY . .

ENTRYPOINT ["python3", "leap.py"]
