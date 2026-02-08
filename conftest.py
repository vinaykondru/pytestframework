"""
conftest.py

This file contains shared pytest fixtures and command-line options used across the framework.

Fixtures included:

1) setup_env (session scope)
   - Loads environment-specific .env file
   - Controlled via: --env=qa/dev/prod

2) browser_setup (class scope)
   - Initializes Selenium WebDriver
   - Supports headless execution
   - Controlled via: --headless

3) pytest_runtest_makereport
    - On failure attaches screenshot on allure report

4) config
    - Loads data based on environment data in YAML files
    - Controlled via: --env=qa/dev/prod

5) setup_env
    - Loads environment-specific .env file
    - Controlled via: --env=qa/dev/prod
Command Line Options:
---------------------
--env        → Select environment (default: qa)
--headless   → Run browser in headless mode

Example runs:
-------------
pytest --env=qa
pytest --env=dev --headless
"""




import datetime
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure
from utils.env_loader import load_env_file
@pytest.fixture(scope="class")
def browser_setup(request,config):
    chrome_options = Options()
    if "headless":
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(config["base_url"])
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = None

        # Case 1: class-based tests
        if hasattr(item, "cls") and item.cls is not None:
            driver = getattr(item.cls, "driver", None)

        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

from utils.config_reader import load_config

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests against"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=True,
        help="Run tests in headless mode"
    )

@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    return load_config(env)

@pytest.fixture(scope="session", autouse=True)
def setup_env(request):
    env_name = request.config.getoption("--env")
    return load_env_file(env_name)