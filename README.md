# SauceDemo QA Automation Framework

## Overview

Automated UI testing framework built with Python, Selenium WebDriver, and Pytest for the SauceDemo e-commerce web application.

## Features

- Valid login testing
- Invalid login testing
- Add item to cart
- Remove item from cart
- Successful checkout flow
- Logout flow
- Full regression suite execution

## Tech Stack

- Python
- Selenium WebDriver
- Pytest

## Project Structure

```text
saucedemo-qa-automation/
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_logout.py
│   └── test_invalid_login.py
├── utils/
│   └── driver_setup.py
├── conftest.py
├── requirements.txt
└── README.md