FROM python:3.8-buster
COPY . /app
EXPOSE 8081
CMD python /app/main.py