# Import the necessary modules
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from data.testdata import SearchEngines   # Import the SearchEngines class
from utilities.logger import LogGen  # Import the LogGen class
from setup_teardown.setup_module import setup
from browser_config import get_browser_driver

# Initialize logger
logger = LogGen.loggen()
BROWSER_NAME = 'chrome'


@pytest.fixture(scope="class")
def setup(request,BROWSER_NAME):
    # Initialize the WebDriver
    driver = get_browser_driver(BROWSER_NAME)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    logger.info("Webdriver Initialized")
    yield
    driver.close()
    driver.quit()
    logger.info("Test Completed - Browser Closed")


@pytest.mark.usefixtures("setup")
class TestSearchEngine:
    @pytest.mark.parametrize('base_url,search_box_name,result_tag,engine_name', SearchEngines.engines)
    def test_search(self, base_url, search_box_name, result_tag, engine_name):
        driver = self.driver
        search_term = "Clover network"

        # Visit the Search Engine
        driver.get(base_url)
        logger.info(f"Opened {engine_name} website")

        # Submit the search term
        search_box = driver.find_element(By.NAME, search_box_name)
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)
        logger.info(f"Submitted search term: {search_term}")

        # Take the first returned item and assert it as the expected result
        first_result = driver.find_element(By.CSS_SELECTOR, result_tag).text
        assert search_term in first_result, f"The search term was not found in the first result on {engine_name}."
        logger.info(f"Search term found in first result on {engine_name}")
