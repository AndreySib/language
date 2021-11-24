import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="es",
                 help="Choose language: es")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    if language == "es":
        print("\nstart language es..")
        browser = webdriver.Chrome()
    else:
        raise pytest.UsageError("--language should be es")
    yield browser
    print("\nquit browser..")
    browser.quit()