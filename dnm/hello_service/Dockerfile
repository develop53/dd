FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY hello_service.py .

EXPOSE 5001

CMD ["python", "hello_service.py"]

