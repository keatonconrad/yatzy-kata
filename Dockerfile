FROM python:3.9-alpine

# Adds user to avoid running as root
RUN addgroup -S yatzy-group
RUN adduser -S yatzy-user -G yatzy-group
ENV PATH "$PATH:/home/yatzy-user/.local/bin"

RUN mkdir /app
COPY . /app
WORKDIR /app

USER yatzy-user

RUN pip3 install pytest

# Disables pytest caching
CMD ["pytest", "-p", "no:cacheprovider"]
