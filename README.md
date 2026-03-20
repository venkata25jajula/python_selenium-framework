# 🚀 Selenium Pytest Automation Framework

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pytest](https://img.shields.io/badge/Pytest-Framework-green)
![Selenium](https://img.shields.io/badge/Selenium-Automation-brightgreen)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-red)
![Allure](https://img.shields.io/badge/Allure-Reporting-orange)

---

## 📌 Overview

This is a **scalable Test Automation Framework** built using:

* **Selenium WebDriver**
* **Pytest**
* **Page Object Model (POM)**
* **Allure Reporting**
* **Jenkins CI/CD Integration**

The framework is designed for **maintainability, reusability, and real-time CI/CD execution**.

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
├── screenshots/          # Allure report screenshots
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
* ✅ GitHub → Jenkins CI/CD integration
* ✅ Real-time test execution via webhooks

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

### ▶️ Generate results

```bash
pytest -v --alluredir=reports/allure-results
```

### ▶️ View report locally

```bash
allure serve reports/allure-results
```

---

## 🌐 Allure Report via Jenkins

Allure reports are automatically published after each Jenkins build.

### 🔗 Sample Report (Local Jenkins)

http://localhost:8080/job/GITHUB%20-%20Python%20Selinium%20Test%20Runner/8/allure/#

---

### 🚀 CI/CD Workflow

```
GitHub → Webhook → Jenkins → Pytest → Allure Results → Allure Report
```

---

### ⚠️ Note

* The above report link works only on **localhost**
* For external access:

  * Use ngrok (temporary public URL)
  * Or deploy Jenkins on cloud (AWS EC2)

---

## 📸 Allure Report Screenshots

### 🟢 Test Execution Overview

![Allure Overview](./screenshots/allure-overview.png)

* ✅ 100% test pass rate
* 🧪 Total test cases executed
* 📊 Execution trends visualization
* 📦 Test suites grouping

---

### 🧩 Test Execution Details

![Allure Details](./screenshots/allure-details.png)

* 📋 Step-by-step execution logs
* ⏱️ Execution time per step
* ✅ Clear pass/fail status
* 🔍 Detailed validation flow

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

* Logs:

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

This framework is fully integrated with Jenkins for automated execution.

### ⚙️ Pipeline Flow

```
GitHub → Webhook → Jenkins → Pytest Execution → Allure Results → Allure Report
```

### 🔧 Key Capabilities

* 🔁 Auto-trigger on GitHub push (webhook-based)
* 🧪 Executes Selenium + Pytest suite
* 📊 Publishes Allure reports after each build
* 📦 Archives logs and test artifacts
* 🌐 Can be exposed publicly using ngrok

---

## 🧠 DevOps Highlights

* ✔️ CI/CD pipeline using Jenkins
* ✔️ GitHub webhook integration
* ✔️ Docker-ready setup
* ✔️ Local Jenkins exposed using ngrok
* ✔️ Scalable for cloud deployment (AWS EC2)

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
* Scalable and maintainable design

---

## 🚀 Future Enhancements

* Parallel execution (pytest-xdist)
* Dockerized test execution
* Cloud execution (AWS / Selenium Grid)
* API + UI combined automation framework

---

## 👨‍💻 Author

**Venkata Apparao Jajula**

---
