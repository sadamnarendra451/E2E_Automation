import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_data_entry_form():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    # Selenium built-in manager వాడటం వల్ల webdriver_manager అవసరం లేదు
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://testautomationpractice.blogspot.com")

        driver.find_element(By.ID, "name").send_keys("Telugu Mawa")
        driver.find_element(By.ID, "email").send_keys("telugumawa@gmail.com")
        driver.find_element(By.ID, "phone").send_keys("9876543210")
        driver.find_element(By.ID, "textarea").send_keys("Hyderabad, Telangana")

        time.sleep(2)
    finally:
        driver.quit()