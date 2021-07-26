FROM python:3.7
MAINTAINER Dima_in_the_forest <dmitrykucev@mail.ru>

ENV INSTALL_PATH /shelter
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
#RUN pip install --editable .

# CMD gunicorn -c "python:config.gunicorn" "shelter.app:create_app()"
#CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "shelter.app:create_app()"