# web-automation-selenium-python
Web UI Automation Using Selenium & Python

Following this guide to run web ui automation project

Pre-con:
1. Install python, I'm using python 3.10.5
2. Install packages to run web ui automation
Open powershell or any cli tool in your root project. 
Run 'python -m venv venv' to create venv (virtual environment) that no depends or affects by others env. Then, activate the env by running this cmd: .\venv\Scripts\activate
Finally, run this cmd: pip install -r requirements.txt --use-pep517

That's all for installation!

How to run tests
Go to root project
* To run all tests: pytest tests
* To run specific test suites, ex: pytest tests\account -v -s
* To run tests in headless mode: pytest tests -v -s --headless=True
* To run tests with specific browser (chrome by default): pytest tests -v -s --browser=chrome 
* To run tests with specific url: pytest tests --url=http:example.com