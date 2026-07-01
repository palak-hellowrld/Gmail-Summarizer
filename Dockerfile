FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY fetch_emails.py ai_Summarizer.py .

CMD ["python", "fetch_emails.py"]


