FROM python:3.14-slim-bookworm

WORKDIR /home/myapp

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip setuptools \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5050

CMD ["python", "sample_app.py"]
