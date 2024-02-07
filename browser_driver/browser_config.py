from selenium import webdriver


def get_browser_driver(browser_name, driver_path='./driver/'):
    """
    Returns the browser driver based on the browser name.

    :param browser_name: Name of the browser (e.g., 'chrome', 'firefox', 'edge', 'safari').
    :param driver_path: Path to the folder containing the WebDriver executables.
    :return: WebDriver instance for the specified browser.
    """
    if browser_name == 'chrome':
        return webdriver.Chrome(executable_path=f'{driver_path}chromedriver')
    elif browser_name == 'firefox':
        return webdriver.Firefox(executable_path=f'{driver_path}geckodriver')
    elif browser_name == 'edge':
        return webdriver.Edge(executable_path=f'{driver_path}msedgedriver')
    elif browser_name == 'safari':
        # SafariDriver comes pre-installed with macOS
        return webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
