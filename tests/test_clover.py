# Import the necessary modules
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from data.testdata import SearchEngines   # Import the SearchEngines class
from Utility.logger import LogGen  # Import the LogGen class
from setup_teardown.setup_module import setup
from browser_driver.browser_config import get_browser_driver
from selenium.common.exceptions import NoSuchElementException, WebDriverException

# Initialize logger
logger = LogGen.loggen()


@pytest.fixture(scope="class")
def setup(request):
    global BROWSER_NAME
    BROWSER_NAME = 'chrome'
    try:
        # Initialize the WebDriver
        driver = get_browser_driver(BROWSER_NAME)
        driver.implicitly_wait(10)
        request.cls.driver = driver
        logger.info("Webdriver Initialized")

    except WebDriverException as e:
        logger.error(f"Error initializing WebDriver: {e}")
        pytest.fail(f"WebDriver initialization failed: {e}")
    yield
    try:
        driver.close()
        driver.quit()
        logger.info("Test Completed - Browser Closed")
    except Exception as e:
        logger.error(f"Error closing the browser: {e}")

@pytest.mark.usefixtures("setup")
class TestSearchEngine:
    @pytest.mark.parametrize('base_url,search_box_name,result_tag,engine_name', SearchEngines.engines)
    def test_search(self, base_url, search_box_name, result_tag, engine_name):
        driver = self.driver
        search_term = "Clover network"
        try:
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
        except NoSuchElementException as e:
            logger.error(f"Element not found: {e}")
            pytest.fail(f"Test failed due to missing element: {e}")
        except Exception as e:
            logger.error(f"Test encountered an error: {e}")
            pytest.fail(f"Test failed due to an unexpected error: {e}")