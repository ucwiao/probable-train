import time
from selenium.webdriver.common.by import By

def auto_schedule(driver):
    print("🛫 Scheduling flights...")
    driver.get("https://www.airlinemanager.com/aircraft")
    time.sleep(5)

    try:
        aircrafts = driver.find_elements(By.CLASS_NAME, "scheduleAllButton")
        for i, a in enumerate(aircrafts):
            try:
                a.click()
                print(f"✅ Scheduled aircraft #{i+1}")
                time.sleep(1)
            except:
                print(f"⚠️ Couldn't schedule aircraft #{i+1}")
    except Exception as e:
        print("❌ Flight error:", e)
      
