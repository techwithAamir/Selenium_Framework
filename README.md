# 🚀 Selenium Python Automation Framework

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-brightgreen?logo=selenium)
![PyTest](https://img.shields.io/badge/PyTest-Framework-orange)
![Jenkins](https://img.shields.io/badge/Jenkins-CI-red?logo=jenkins)
![Git](https://img.shields.io/badge/Git-Version%20Control-orange?logo=git)
![License](https://img.shields.io/badge/License-MIT-success)

</p>

---

# 📌 Overview

This repository contains a **Production-Ready Selenium Automation Framework** built using **Python**, **PyTest**, and the **Page Object Model (POM)**.

The framework follows industry-standard automation practices to create scalable, reusable, and maintainable UI test automation. It supports **cross-browser execution**, **data-driven testing**, **HTML reporting**, **automatic screenshot capture**, and **Jenkins Continuous Integration**.

---

# ✨ Features

- ✅ Selenium WebDriver
- ✅ Python Automation
- ✅ PyTest Framework
- ✅ Page Object Model (POM)
- ✅ Data-Driven Testing (JSON)
- ✅ Cross Browser Testing
- ✅ HTML Reports
- ✅ Screenshot Capture on Failure
- ✅ Explicit & Implicit Waits
- ✅ Jenkins CI Integration
- ✅ Git Version Control
- ✅ Modular Framework Design
- ✅ Reusable Browser Utilities
- ✅ Parameterized Test Execution
- ✅ Easy Maintenance

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Selenium WebDriver | Browser Automation |
| PyTest | Test Framework |
| JSON | Test Data Management |
| Jenkins | Continuous Integration |
| Git | Version Control |
| GitHub | Source Code Management |
| HTML Reports | Test Reporting |

---

# 📂 Project Structure

```
Framework
│
├── Data
│   └── test_e2eFrame.json
│
├── pageObjects
│   ├── login.py
│   ├── shop.py
│   └── checkout_confirmation.py
│
├── reports
│
├── utils
│   └── browserutils.py
│
├── conftest.py
│
└── test_e2eFrame.py
```

---

# 🏗 Framework Architecture

```
Test Cases
     │
     ▼
PyTest Framework
     │
     ▼
Page Object Model
     │
     ▼
Selenium WebDriver
     │
     ▼
Browser Driver
     │
     ▼
Web Browser
```

---

# 📁 Folder Description

## Data

Contains JSON files used for Data-Driven Testing.

---

## pageObjects

Implements the **Page Object Model** where every webpage has its own Python class.

- login.py
- shop.py
- checkout_confirmation.py

---

## reports

Stores generated HTML Reports and failure screenshots.

---

## utils

Contains reusable browser utility functions.

---

## conftest.py

Contains

- Browser Fixture
- Browser Selection
- Screenshot Capture
- HTML Report Configuration
- PyTest Hooks

---

## test_e2eFrame.py

Main End-to-End Test Script.

---

# 🚀 Supported Browsers

- Microsoft Edge
- Google Chrome
- Mozilla Firefox

Example

```bash
pytest -v -s test_e2eFrame.py --browser_name=edge
```

```bash
pytest -v -s test_e2eFrame.py --browser_name=chrome
```

```bash
pytest -v -s test_e2eFrame.py --browser_name=firefox
```

---

# 📊 Data Driven Testing

Test data is stored inside JSON.

Example

```json
[
    {
        "userEmail":"rahulshettyacademy",
        "userPassword":"learning",
        "productName":"iphone X"
    }
]
```

This enables executing the same test with multiple datasets without changing the test logic.

---

# 📸 Screenshot Capture

Whenever a test fails,

the framework automatically

- Captures Screenshot
- Stores Screenshot
- Embeds Screenshot into HTML Report

making debugging easier.

---

# 📈 HTML Report

Generate HTML Report

```bash
pytest -v -s test_e2eFrame.py --browser_name=edge --html=reports/report.html --self-contained-html
```

---

# ⚙ Jenkins Integration

The framework supports Continuous Integration using Jenkins.

Example Batch Command

```bat
cd /d "C:\Users\MD AAMIR\.vscode\Testing"

"C:\Users\MD AAMIR\.vscode\Testing\venv\Scripts\python.exe" -m pytest -v -s Framework/test_e2eFrame.py --browser_name=edge --html=Framework/reports/report.html --self-contained-html
```

The framework automatically

- Executes Tests
- Generates Reports
- Publishes HTML Reports
- Maintains Build History

---

# 📦 Installation

Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Selenium-Python-Automation-Framework.git
```

Move into Project

```bash
cd Selenium-Python-Automation-Framework
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running Tests

Run Complete Suite

```bash
pytest -v -s
```

Run End-to-End Test

```bash
pytest test_e2eFrame.py
```

Run with Edge

```bash
pytest -v -s test_e2eFrame.py --browser_name=edge
```

Run with Chrome

```bash
pytest -v -s test_e2eFrame.py --browser_name=chrome
```

Run with Firefox

```bash
pytest -v -s test_e2eFrame.py --browser_name=firefox
```

---

# 📚 Automation Concepts Covered

- Selenium WebDriver
- Python
- PyTest
- Fixtures
- Assertions
- Page Object Model
- Data Driven Testing
- JSON
- Cross Browser Testing
- Explicit Wait
- Implicit Wait
- Screenshot Capture
- HTML Reports
- Jenkins CI
- Git
- Version Control

---

# 🎯 Future Enhancements

- Docker Integration
- GitHub Actions CI/CD
- Allure Reports
- Parallel Test Execution
- Logging Framework
- Retry Failed Tests
- Excel Data Provider
- API Testing Integration

---

# 👨‍💻 Author

## MD AAMIR

**Aspiring QA Automation Engineer**

### Skills

- Selenium
- Python
- PyTest
- Jenkins
- Git
- SQL
- Manual Testing
- Automation Testing
- Page Object Model
- Data Driven Testing

---

# 🙏 Acknowledgements

A sincere thank you to **Rahul Shetty Academy** for providing an industry-oriented Selenium automation course, interview preparation materials, and practical guidance that helped me build this framework following real-world QA automation practices.

---

# ⭐ Support

If you found this project useful,

please consider giving it a ⭐ Star.

It motivates me to keep building and sharing more automation projects.

---


## 📄 License

This project is licensed under the MIT License.
