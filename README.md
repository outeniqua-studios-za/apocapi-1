# apocapi
I am a python web and mobile test automation framework

### Prerequistes

- Nodejs (for Appium)
- Python 3.*
- Pytest

### Usage:

- Setup venv
- Install selenium package ``` pip install selenium ```
- Install appium server ``` npm install -g appium ```
- Install appium client package ``` pip install Appium-Python-Client ```
- To run appium server execute ``` appium ```
- Run ``` py.test -s -v tests/%folder/teststorun%.py ``` from project root
- Results are logged in ``` testresults.log ```
- Screenshots are stored in ``` screenshots ``` folder for failed tests

