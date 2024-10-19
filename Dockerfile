FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY my_rest_api.py .

CMD ["uvicorn", "my_rest_api:app", "--host", "0.0.0.0", "--port", "10000"]