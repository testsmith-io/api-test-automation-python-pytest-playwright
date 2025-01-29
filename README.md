# API Test Automation with Python, Pytest, and Playwright

[![API Test Automation with Python, Pytest, and Playwright - Run Tests](https://github.com/testsmith-io/api-test-automation-python-pytest-playwright/actions/workflows/pytest.yml/badge.svg)](https://github.com/testsmith-io/api-test-automation-python-pytest-playwright/actions/workflows/pytest.yml)

This repository contains example scripts for API test automation using:
- **Python**
- **Playwright** for API interaction
- **Pytest** for test execution

## Features
- Examples of GET, POST, and Protected API requests.
- Clear demonstration of API test automation practices with assertions and chaining requests.
- Fully automated CI pipeline using GitHub Actions.

## Test API
All examples in this repository are designed to work with the **Practice Software Testing API**, a publicly available API for learning and practicing software testing. You can explore the API documentation and endpoints here:  
👉 **[Practice Software Testing API](https://api.practicesoftwaretesting.com/api/documentation)** 👈

## Examples Included
1. **GET Request**: Fetch a list of brands with `GET /brands`.
2. **Login API**: Authenticate using `POST /login` with an email/password payload.
3. **Protected API Request**: Authenticate, then use a token to fetch data with `GET /invoices`.

## Prerequisites
- **Python 3.8+**
- **pip (Python package manager)**
- **Playwright installed** (See setup instructions below)

## Setup and Run
1. Clone this repository:
   ```bash
   git clone https://github.com/testsmith-io/api-test-automation-python-pytest-playwright.git
   ```
2. Navigate to the project directory:
   ```bash
   cd api-test-automation-python-pytest-playwright
   ```
3. Set Up a Virtual Environment (Optional, Recommended)
Using a virtual environment ensures that dependencies for this project are isolated from your global Python environment.

#### Create a Virtual Environment

In VS Code open the Command Palette (MacOs: `CMD` + `SHIFT` + `P`, Windows: `CTRL` + `SHIFT` + `P`)

- In the Command Palette, type and select/type: `Python: Select Interpreter`.
- Choose the Python interpreter you want to use from the list OR create a new
one.

This ensures VS Code uses the virtual environment for running and debugging.

4. Install Dependencies
Once the virtual environment is active:
```bash
pip install -r requirements.txt
```

   ```
5. Run the tests:
   ```bash
   pytest
   ```

## Automated Workflow
The repository includes a GitHub Actions workflow to automatically run tests on every push and pull request.