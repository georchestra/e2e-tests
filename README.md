# geOrchestra Playwright Tests

![build-and-tests](https://github.com/georchestra/e2e-tests/actions/workflows/build-and-tests.yml/badge.svg)

Report : https://www.georchestra.org/e2e-tests

This project contains automated tests for the geOrchestra web applications using Playwright and pytest.

## Prerequisites

- Python 3.11
- pip (Python package installer)
- Docker

## Setup

1. Install the dependencies:
    ```sh
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

2. Ensure Playwright browsers are installed:
    ```sh
    python -m playwright install --with-deps
    ```
   
3. (If georchestra/docker isn't already cloned) Start the geOrchestra services using Docker:
    ```sh
    git clone https://github.com/georchestra/docker.git
    cd docker
    docker compose up -d --wait
    cd ..
    wget "https://caddyserver.com/api/download?os=linux&arch=amd64" -O caddy
      chmod +x caddy
    ./caddy trust
    ```
4. Change base url in `pytest.ini` file to match your local geOrchestra instance:
 ```ini
[pytest]
addopts = --base-url=https://georchestra-127-0-0-1.nip.io
 ```

## Help to generate a test

To help generate a new test, you can use the following command:
```sh
python -m playwright codegen https://<your-sdi>
```
It will open a browser and you can interact with the website. At the end, it will generate a Python script with the interactions you made.

## Running Tests

To run the tests locally, use the following command:
```sh
pytest tests --alluredir=allure-results --headed
```

Remove the `--headed` flag to run the tests in headless mode.

## Generate allure report

To generate the allure report, use the following command:
```sh
allure serve allure-results
```

## How to use base image and run specific tests 

Create a folder where you put your specific tests and create a Dockerfile with the following content:

```Dockerfile
FROM georchestra/e2e-tests:latest

COPY mytests /app/tests/mytests
```