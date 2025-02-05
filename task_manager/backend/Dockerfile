FROM python:3.10-slim

WORKDIR /task_manager_backend

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]