FROM python:3.12-bookworm

RUN pip install playwright && \
    playwright install --with-deps

COPY . /app
WORKDIR /app

CMD ["python", "/app/test_example.py"]