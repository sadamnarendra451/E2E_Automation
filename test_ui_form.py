import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_data_entry_form():
    # Headless mode setup (Screen leni GitHub Runner kosam)
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://testautomationpractice.blogspot.com")[span_0](start_span)[span_0](end_span)

    driver.find_element(By.ID, "name").send_keys("Telugu Mawa")
    driver.find_element(By.ID, "email").send_keys("telugumawa@gmail.com")
    driver.find_element(By.ID, "phone").send_keys("9876543210")
    driver.find_element(By.ID, "textarea").send_keys("Hyderabad, Telangana")

    time.sleep(2)
    driver.quit()