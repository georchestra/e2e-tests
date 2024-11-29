# geOrchestra Playwright Tests

This project contains automated tests for the geOrchestra web applications using Playwright and pytest.

## Project Structure

- `tests/`: Contains the test files.
- `conftest.py`: Configuration file for pytest fixtures.
- `.github/workflows/playwright.yml`: GitHub Actions workflow for running the tests.

## Prerequisites

- Python 3.11
- pip (Python package installer)
- Docker

## Setup

1. Install the dependencies:
    ```sh
    python -m pip install --upgrade pip
    pip install -r tests/requirements.txt
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
