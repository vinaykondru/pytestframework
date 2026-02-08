# Selenium + Pytest Automation Framework

## 📌 Overview

This project is a scalable Selenium automation framework built using **Python + Pytest**, following the **Page Object Model (POM)** design pattern.
The framework is structured to keep test logic, page actions, and utilities cleanly separated for better maintainability and readability.

It supports:

* Environment-based execution (`--env=qa/dev`)
* Headless/Headed mode (`--headless`)
* Secure credential handling using `.env`
* Data-driven testing using CSV/JSON
* Reusable utilities and fixtures

---

## 🧱 Framework Architecture

The framework follows a layered design:

```
project/
│
├── pages/            → Page classes (POM)
├── tests/            → Test classes
├── utils/            → Utility/helper functions
├── config/           → Environment configs (YAML)
├── secrets/          → .env files (ignored in git)
├── testdata/         → CSV/JSON test data
├── conftest.py       → Fixtures & CLI options
└── README.md
```

---

## 📂 Folder Responsibilities

### 📁 `pages/` – Page Object Model (POM)

Contains all page classes representing UI screens.

Each class includes:

* Locators
* Page actions
* Reusable methods

Example:

```
pages/
   login_page.py
   dashboard_page.py
```

Example structure:

```python
class LoginPage:
    def enter_username(self, username): ...
    def enter_password(self, password): ...
    def click_login(self): ...
```

This keeps UI logic separate from test logic.

---

### 📁 `tests/` – Test Classes

Contains actual test scenarios.

Each test:

* Calls page methods
* Contains assertions
* Represents a business flow

Example:

```
tests/
   test_login.py
   test_checkout.py
```

Tests remain clean and readable because UI actions are handled in page classes.

---

### 📁 `utils/` – Utilities & Helpers

Contains reusable support functions such as:

* Loading `.env` secrets
* Reading YAML config
* Reading CSV/JSON test data
* Common helpers

Example:

```
utils/
   env_loader.py
   config_reader.py
   data_reader.py
```

---

### 📁 `config/` – Environment Configuration

Stores environment-specific settings.

Example:

```
config/
   qa.yaml
   dev.yaml
```

Contains:

* Base URLs
* Browser settings
* Timeouts
* Non-sensitive config

---

### 📁 `secrets/` – Environment Secrets

Stores sensitive values (not committed to Git):

```
secrets/
   .env.qa
   .env.dev
```

Contains:

```
LOGIN_USERNAME=
LOGIN_PASSWORD=
API_KEY=
```

⚠️ These files are ignored using `.gitignore`.

---

### 📁 `testdata/` – Test Data

Stores data-driven inputs.

Formats supported:

* CSV → bulk test cases
* JSON → structured data

Example:

```
testdata/
   login_data.csv
   users.json
```

---

## ⚙️ Fixtures (conftest.py)

Centralized test setup includes:

* Environment loader
* Browser initialization
* Headless support
* Shared fixtures

Command-line options:

```
--env=qa/dev        → Select environment
--headless          → Run without UI
```

---

## ▶️ How to Run Tests

### Default run

```
pytest
```

### Run on QA environment

```
pytest --env=qa
```

### Run in headless mode

```
pytest --env=qa --headless
```

---

## 🔐 Security Best Practices

* `.env` files are NOT committed
* `.env.example` is provided as template
* Secrets loaded at runtime

Add to `.gitignore`:

```
.env.*
secrets/.env.*
```

---

## 🧪 Design Principles Followed

* Page Object Model (POM)
* Separation of concerns
* Reusable fixtures
* Environment-driven execution
* Secure credential handling
* Data-driven testing support

---

## 👨‍💻 Author Notes

This framework is designed to demonstrate:

* Strong understanding of Selenium automation
* Clean architecture using POM
* Practical industry standards
* Scalable test structure
* Maintainable test design
