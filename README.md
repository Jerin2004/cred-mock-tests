# 🚀 CRED Mock API Testing Suite

![Project Banner](assets/banner.png) <!-- Add your banner image here -->

A professional-grade API testing framework demonstrating automated testing practices for CRED-like financial applications.

## 🧰 Tech Stack
![Python](https://img.shields.io/badge/Python-3.13%2B-blue)
![Pytest](https://img.shields.io/badge/Pytest-7.4.0-green)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub_Actions-orange)

## 📌 Key Features
- ✔️ Automated API contract testing
- ✔️ CI/CD integration
- ✔️ HTML test reporting
- ✔️ Negative test case validation

## 📸 Screenshots
| Test Report | CI/CD Pipeline |
|------------|----------------|
| ![Test Report](assets/report-screenshot.png) | ![CI/CD](assets/ci-cd-screenshot.png) |

## 🛠️ Setup Guide

### Prerequisites
```bash
pip install -r requirements.txt

# Run all tests with HTML reporting
pytest api_tests/ --html=reports/report.html --self-contained-html

📂 Project Structure
cred-mock-tests/
├── api_tests/           # Test scripts
├── reports/             # Generated test reports
├── assets/              # Images/screenshots <-- PUT YOUR IMAGES HERE
├── .github/workflows/   # CI/CD pipelines
└── requirements.txt     # Dependencies

