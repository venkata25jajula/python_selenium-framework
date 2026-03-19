# 🚀 Selenium Pytest Automation Framework

## 📌 Overview

This is a **scalable Test Automation Framework** built using:

* **Selenium WebDriver**
* **Pytest**
* **Page Object Model (POM)**
* **Allure Reporting**

The framework is designed for **maintainability, reusability, and CI/CD integration (Jenkins-ready)**.

---

## 🏗️ Project Structure

```
project/
│
├── configs/              # Configuration files (INI, readers)
├── pages/                # Page Object Model classes
├── tests/                # Test cases
├── utils/                # Utilities (logger, driver factory, helpers)
│
├── logs/                 # Execution logs (ignored in Git)
├── reports/              # Test reports (ignored in Git)
├── allure-report/        # Allure HTML report (ignored)
│
├── conftest.py           # Pytest fixtures
├── pytest.ini            # Pytest configuration
├── TestRunner.py         # Custom test runner
├── requirements.txt      # Dependencies
└── .gitignore
```

---

## ⚙️ Features

* ✅ Page Object Model (POM) design pattern
* ✅ Centralized WebDriver management
* ✅ Custom logging with timestamps
* ✅ Pytest fixtures for setup/teardown
* ✅ Allure reporting with screenshots
* ✅ Config-driven execution
* ✅ Jenkins/CI ready

---

## 🧪 Test Execution

### ▶️ Run using Pytest

```bash
pytest -v
```

### ▶️ Run using TestRunner

```bash
python TestRunner.py
```

---

## 📊 Allure Reporting

### Generate results

```bash
pytest --alluredir=reports/allure-results
```

### View report

```bash
allure serve reports/allure-results
```

---

## 🔧 Configuration

Update environment settings in:

```
configs/config.ini
```

Example:

```ini
[DEFAULT]
base_url = https://www.saucedemo.com/
browser = chrome
```

---

## 📸 Logging & Reports

* Logs are generated under:

```
logs/
```

* Allure results:

```
reports/allure-results/
```

* HTML report:

```
allure-report/
```

---

## 🧰 Utilities

* `driver_factory.py` → WebDriver setup
* `logger.py` → Logging utility
* `page_factory.py` → Page object initialization
* `utilities.py` → Common helper methods

---

## 🧪 Sample Test Flow

1. Launch application
2. Login
3. Navigate to inventory
4. Add items to cart
5. Checkout & payment
6. Validate order confirmation

---

## 🔄 CI/CD Integration (Jenkins)

* Execute tests via `TestRunner.py`
* Publish Allure reports
* Archive logs & artifacts

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

---

## ✅ Best Practices Followed

* Separation of concerns
* Reusable components
* Clean folder structure
* Git ignore for non-essential files
* Scalable design

---

## 👨‍💻 Author

**Venkata Apparao Jajula**

---

## 🚀 Future Enhancements

* Parallel execution (pytest-xdist)
* Docker integration
* Cloud execution (AWS / Selenium Grid)
* API + UI combined framework

---
