import pytest
import os
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current file
    driver_path = os.path.join(base_dir, 'browsers', 'chromedriver')  # Construct the path to chromedriver

    # Initialize the WebDriver
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
