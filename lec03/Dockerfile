FROM python:3.9.16-alpine3.16

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt 

EXPOSE 8081
CMD ["python", "with_session.py"]