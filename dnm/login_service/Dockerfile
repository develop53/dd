FROM python:3.9-slim

WORKDIR /app

# Gerekli Python bağımlılıklarını yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY login_service.py .

EXPOSE 5000

CMD ["python", "login_service.py"]

