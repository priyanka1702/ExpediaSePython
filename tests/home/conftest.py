import pytest
from base.webdriverfactory import Webdriverfactory
# Normal setup - module level
@pytest.fixture()
def setup():
    print("Setup - Runs before test.")
    yield
    print("Setup - runs after test.")


# Class level setup with passing arguments and returning values
@pytest.fixture(scope="class")
def CLSetup_returnvalue(request,browser):
    print("Class Level - Setup - Runs before test.")
    wdf = Webdriverfactory(browser)
    driver = wdf.getdriverInstance()
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Class Level - Setup - runs after test.")

# Adding option
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType",help="Type of Operating System")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")