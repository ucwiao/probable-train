from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json, time

def get_driver():
    options = Options()
    options.add_argument("--headless")  # remove if you want to see the browser
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)

def load_credentials():
    with open("config/credentials.json") as f:
        return json.load(f)

def login(driver):
    creds = load_credentials()
    driver.get("https://www.airlinemanager.com/")
    
    try:
        # Wait for email field
        email_input = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, "lEmail"))
        )
        email_input.clear()
        email_input.send_keys(creds["email"])

        # Wait for password field
        password_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "lPass"))
        )
        password_input.clear()
        password_input.send_keys(creds["password"])

        # Click login button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btnLogin"))
        )
        login_button.click()

        # Wait until dashboard or main page loads
        time.sleep(5)
        if "dashboard" in driver.current_url or "airline" in driver.current_url:
            print("✅ Successfully logged in!")
            return True
        else:
            print("⚠️ Login attempted but URL didn’t change. Check credentials.")

    except Exception as e:
        print(f"❌ Login failed: {e}")
    
    return False
    
