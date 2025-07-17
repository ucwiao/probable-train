import json, time
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

def load_credentials():
    with open("config/credentials.json") as f:
        return json.load(f)

def get_driver():
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return uc.Chrome(options=options)

def login(driver):
    creds = load_credentials()
    driver.get("https://www.airlinemanager.com/")
    time.sleep(5)

    try:
        driver.find_element(By.ID, "email").send_keys(creds["email"])
        driver.find_element(By.ID, "password").send_keys(creds["password"])
        driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
        time.sleep(6)
        if "dashboard" in driver.current_url:
            print("✅ Login success")
            return True
    except Exception as e:
        print("❌ Login error:", e)

    return False
  
