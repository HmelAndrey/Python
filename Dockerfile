FROM python:3

COPY requirements.txt .
COPY app.py .
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "app.py"]
