FROM python:3.9
WORKDIR /SSapi (1)
RUN apt-get update && \
    apt-get install -y portaudio19-dev
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /SSapi (1)/
CMD ["python","SSapi (1).py"]
