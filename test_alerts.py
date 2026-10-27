import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_alert_popup():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # వెబ్ సైట్ ఓపెన్ చేయడం
        driver.get("https://testautomationpractice.blogspot.com")

        # అలెర్ట్ బాక్స్ ఓపెన్ చేసే బటన్ మీద క్లిక్ చేయడం
        alert_button = driver.find_element(By.ID, "alertBtn")
        alert_button.click()
        time.sleep(1)

        # బ్రౌజర్ అలెర్ట్ (Pop-up) ని స్విచ్ చేసి యాక్సెప్ట్ (OK) చేయడం
        alert = driver.switch_to.alert
        print("Alert Message:", alert.text)
        alert.accept()

        print("Alert test passed successfully!")
    finally:
        driver.quit()