FROM alpine:latest
# COPY . /app
EXPOSE 5000
VOLUME /usr/src/app/public
WORKDIR /usr/src/app

RUN apk add --no-cache --update-cache --repository http://nl.alpinelinux.org/alpine/v3.8/main alsa-lib-dev=1.1.6-r0 \
    && apk add cmd:pip3 \
    && apk add --no-cache python3-dev \
    && pip3 install --upgrade pip \
    && apk add --update --no-cache g++ gcc libxslt-dev \
    && apk add --no-cache \
        uwsgi-python3 \
        python3 \
    && pip3 --no-cache-dir install lxml flask requests Jinja2

# WORKDIR  /app

COPY . .
ADD . /usr/src/app
RUN rm -rf public/*
# RUN pip install -r requirements.txt
# ENTRYPOINT [ "python3" ]
# CMD ["main.py"]
CMD ["uwsgi","uwsgi.ini"]
