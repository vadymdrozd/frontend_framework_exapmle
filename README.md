# StreamLayer GUI tests

UI autotests for authorization, reset password and event moderation flows built with Python, Pytest, Selenium and Allure.

## Tech stack

- Python 3
- Pytest
- Selenium
- Allure
- Docker / Docker Compose

## Project structure

- `tests/` — test suites
- `pages/` — Page Object classes and locators
- `core/config/` — project configuration
- `core/test_data/` — csv datasets for parametrized tests
- `conftest.py` — shared fixtures, webdriver setup, screenshots on failures
- `allureport/` / `allure-results/` — generated Allure results
- `screenshots/` — screenshots directory placeholder

## Local run

### 1. Create virtual environment

```bash
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

Or use helper script:

```bash
bash ./activation.sh
```

### 2. Run all tests

```bash
pytest .
```

### 3. Run specific suites

Authorization:

```bash
pytest tests/authorization -m authorization
```

Reset password:

```bash
pytest tests/reset_password -m reset_password
```

Event moderation:

```bash
pytest tests/event_moderation -m moderation
```

### 4. Run with Allure results

```bash
pytest . --alluredir allure-results/local
```

## Docker run

Build and run:

```bash
docker compose up --build
```

Inside container, tests are started by `entrypoint.sh` with command:

```bash
python -m pytest . --alluredir allure-results/${REVISION}
```

## Test data

CSV files for parametrized tests are stored in:

- `core/test_data/authorization/`
- `core/test_data/event_moderation/`

## Markers

Configured in `pytest.ini`:

- `acceptance`
- `authorization`
- `reset_password`
- `moderation`

## Important notes

- Current shared fixture in `conftest.py` starts local Chrome via `webdriver-manager`.
- Selenium container `chrome_webdriver` is described in `docker-compose.yaml`, but remote driver usage is currently commented out in the code.
- Browser runs in headless mode.
- Failed tests attach screenshots to Allure report.
- Event moderation fixture contains hardcoded login credentials and opens moderation page after UI login.
- Base URL is configured in `core/config/webdriver_config.py`.

## Main URLs from config

- Base URL: `https://studio-13.next.streamlayer.io/`
- Authorization page: `sign-in`
- Reset password page: `reset-password/email`
- Moderation page: `events/all/id/509/moderation`
