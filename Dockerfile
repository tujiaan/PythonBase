FROM python:3.6
LABEL maintainer="Kaive Young <kaiveyoung@gmail.com>"
WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./patch/flask_security/core.py /usr/local/lib/python3.6/site-packages/flask_security
VOLUME /usr/src/app
EXPOSE 80
CMD [ "gunicorn", "-b","0.0.0.0:80","-w","2","run:application" ]