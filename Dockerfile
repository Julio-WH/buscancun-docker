FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Instalar las dependencias de Ubuntu
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv nginx supervisor

WORKDIR /code

COPY requeriments.txt /code/
RUN pip3 install --no-cache-dir -r requeriments.txt

#Supervisor
COPY supervisord/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
