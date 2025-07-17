import json, time
from selenium.webdriver.common.by import By

def load_config():
    with open("config/fuel_config.json") as f:
        return json.load(f)

def auto_fuel(driver):
    cfg = load_config()
    driver.get("https://www.airlinemanager.com/fuel")
    time.sleep(5)

    try:
        price = float(driver.find_element(By.ID, "fuelPrice").text.replace(",", ""))
        if price <= cfg["buy_threshold"]:
            qty = str(cfg["max_fuel_to_buy"])
            driver.find_element(By.ID, "fuelAmount").clear()
            driver.find_element(By.ID, "fuelAmount").send_keys(qty)
            driver.find_element(By.ID, "buyFuelBtn").click()
            print(f"🛢️ Bought {qty} fuel at {price}")
        else:
            print(f"⛽ Fuel price {price} too high. No buy.")
    except Exception as e:
        print("❌ Fuel error:", e)
      
