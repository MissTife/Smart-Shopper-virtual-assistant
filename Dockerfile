FROM python:3.9-slim-buster
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libportaudio2 \
    libportaudiocpp0 \
    portaudio19-dev \
    && rm -rf /var/lib/apt/lists/*
    
WORKDIR /SSapi (1)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "SSapi (1).py"]    
