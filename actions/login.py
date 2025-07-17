import json, time
from selenium.webdriver.common.by import By

def load_credentials():
    with open("config/credentials.json") as f:
        return json.load(f)

def login(driver):
    creds = load_credentials()
    driver.get("https://www.airlinemanager.com/")
    time.sleep(5)

    try:
        driver.find_element(By.ID, "lEmail").send_keys(creds["email"])
        driver.find_element(By.ID, "lPass").send_keys(creds["password"])
        driver.find_element(By.ID, "btnLogin").click()
        time.sleep(5)

        if "dashboard" in driver.current_url or "airline" in driver.current_url:
            print("✅ Successfully logged in!")
            return True
        else:
            print("⚠️ Login attempted but URL didn’t change. Check credentials.")
    except Exception as e:
        print("❌ Login failed:", e)
    return False
    
