import json, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 🔐 Load login credentials
def load_credentials():
    with open("config/credentials.json") as f:
        return json.load(f)

# 🚀 Launch headless Chrome driver
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=chrome_options)

# 🔐 Login to AM4 with Selenium
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
    
