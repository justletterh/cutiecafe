FROM python:3.8-alpine
RUN apk add build-base libffi-dev
RUN python3 -m pip install -U pip discord.py jishaku psutil
# Add stuff below this line
# Example:
RUN apk add bash
# (That enables jsk sh)
