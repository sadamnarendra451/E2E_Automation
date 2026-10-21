import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_data_entry_form():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://testautomationpractice.blogspot.com")

    driver.find_element(By.ID, "name").send_keys("Telugu Mawa")
    driver.find_element(By.ID, "email").send_keys("telugumawa@gmail.com")
    driver.find_element(By.ID, "phone").send_keys("9876543210")
    driver.find_element(By.ID, "textarea").send_keys("Hyderabad, Telangana")

    time.sleep(2)
    driver.quit()