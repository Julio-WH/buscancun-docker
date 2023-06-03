FROM ubuntu:latest
ENV PYTHONUNBUFFERED 1

# Instalar las dependencias de Ubuntu
RUN apt-get update && \
    apt-get install -y python3 python3-pip nginx

# Instalar Django
RUN pip3 install Django==3.2
#COPY . /code
WORKDIR /code

# Configurar Nginx


# Exponer el puerto 80 para Nginx
#EXPOSE 80

# Ejecutar Nginx y el servidor Django cuando se inicie el contenedor
#CMD sudo /etc/init.d/nginx stop && sudo /etc/init.d/nginx start
