# QA Automation Prototype

A lightweight QA automation framework showcasing:
- **Python + Playwright** for web testing (Latham & Watkins site)
- **Requests + Pytest** for API testing
- **Page Object Model (POM)** for scalable design
- **CI/CD with GitHub Actions** for continuous validation

## Features
✅ Homepage + search validation on Latham & Watkins  
✅ API CRUD testing with jsonplaceholder  
✅ CI pipeline generating HTML test reports  
✅ Configurable + extendable structure  

## Run Locally
```bash
pip3 install -r requirements.txt
pytest --html=reports/test-report.html --self-contained-html

