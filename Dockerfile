FROM python:3-slim
ENV BASE_URL=https://georchestra-127-0-0-1.nip.io

COPY . /app

WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m playwright install --with-deps

ENTRYPOINT pytest --base-url=$BASE_URL