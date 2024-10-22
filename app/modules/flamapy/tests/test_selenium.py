from selenium.common.exceptions import NoSuchElementException
import time

from selenium import webdriver
from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import close_driver


def test_flamapy_index():

    driver = webdriver.Chrome()

    try:
        host = get_host_for_selenium_testing()

        # Open the index page
        driver.get(f'{host}/flamapy')

        # Wait a little while to make sure the page has loaded completely
        time.sleep(4)

        try:

            pass

        except NoSuchElementException:
            raise AssertionError('Test failed!')

    finally:

        # Close the browser
        close_driver(driver)


# Call the test function
test_flamapy_index()
