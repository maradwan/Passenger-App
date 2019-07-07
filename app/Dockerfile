FROM python:3.6

# Place app in container.
COPY . /opt/www
WORKDIR /opt/www

# Install dependencies.
RUN pip install -r requirements.txt

EXPOSE 5000
CMD [ "uwsgi", "--ini", "app.ini" ]
