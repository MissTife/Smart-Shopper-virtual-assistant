FROM python:3.9-slim-buster
RUN apt-get update && \
    apt-get install -y build-essential python3-dev libasound2-dev
RUN pip install -U pip && \
    pip install wheel && \
    pip wheel --wheel-dir=/wheels pyaudio
