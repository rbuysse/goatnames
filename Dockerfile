FROM alpine:3.5.2

RUN apk update && \
	apk add python \
	py-pip \
	git && \
	pip install tweepy

RUN git clone https://github.com/rbuysse/twitterbot.git

WORKDIR twitterbot

RUN python setup.py install

ADD data/GOATNAMES /twitterbot/twitterbot/data/
ADD *.py /twitterbot/twitterbot/

WORKDIR /twitterbot/twitterbot

CMD python goatbot.py
