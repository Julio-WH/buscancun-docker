FROM ubuntu:latest
ENV PYTHONUNBUFFERED 1

# Instalar las dependencias de Ubuntu
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv nginx supervisor

# Instalar Django
RUN pip3 install Django==3.2

WORKDIR /code

#Supervisor
COPY supervisord/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]
