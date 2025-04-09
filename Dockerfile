FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libqt5gui5 \
    libqt5widgets5 \
    libqt5core5a \
    libqt5network5 \
    libxcb-xinerama0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV MODEL_PATH=src/data/train/weights/best.pt

CMD ["python", "src/main.py"]
