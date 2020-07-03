FROM python:3.8-alpine

RUN apk add --no-cache build-base libffi-dev zlib-dev jpeg-dev cairo-dev
RUN pip install -U pip cairosvg discord.py[voice] jishaku psutil
RUN apk add bash