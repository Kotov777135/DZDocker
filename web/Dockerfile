FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY webser.py .

EXPOSE 8000

CMD python3 webser.py
