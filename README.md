# 🧪 Network Automation Testing Framework

![GitHub last commit](https://img.shields.io/github/last-commit/Vinayak18072003/Network-Automation-Testing-Framework)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Python Version](https://img.shields.io/badge/python-3.11-blue)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux-blue)


## 📘 Overview
This project automates basic network connectivity and latency tests using **Robot Framework** and **Python**.  
It simulates how network test engineers automate repetitive test cases during telecom testing.

## ⚙️ Tech Stack
- Python  
- Robot Framework  
- Ping3 Library  
- SSHLibrary (for remote access)

## 🚀 Features
- Automated ping & latency tests  
- Robot Framework HTML reports  
- Modular keyword-based design  
- Extendable for LTE/5G testing scripts  

## 🧩 How to Run
```bash
git clone https://github.com/Vinayak18072003/Network-Automation-Testing-Framework.git
cd Network-Automation-Testing-Framework
pip install -r requirements.txt
python run_tests.py

## 🧪 Sample Output

When running `python run_tests.py`, a Robot Framework report is generated in `/results/`.

Example console output:


Example test summary (from report.html):

| Test Name | Status | Latency (ms) |
|------------|--------|--------------|
| Ping Network Host | ✅ PASS | 36.42 |
| Measure Latency | ✅ PASS | 36.42 |

## 📸 Report Preview
![Test Report Screenshot](screenshots/report_preview.png)

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!  
Feel free to **fork** this repo and open a **pull request**.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🐞 Known Issues / To-Do
- Add SSH-based remote testing support  
- Integrate CI/CD pipeline using GitHub Actions  
- Support for multiple hosts & test scheduling

