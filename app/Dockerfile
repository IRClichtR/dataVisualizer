FROM python:3.9-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /app
# COPY requirements.txt requirements.txt
# COPY entrypoint.sh entypoint.sh
COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt 

RUN chmod +x entrypoint.sh
EXPOSE 8000

ENTRYPOINT ["/bin/sh", "-c", "/app/entrypoint.sh"]

