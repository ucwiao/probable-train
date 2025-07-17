import json, time
from selenium.webdriver.common.by import By

def load_config():
    with open("config/aircraft_config.json") as f:
        return json.load(f)

def auto_buy_aircraft(driver):
    cfg = load_config()
    driver.get("https://www.airlinemanager.com/aircraft/buy")
    time.sleep(5)

    try:
        models = driver.find_elements(By.CLASS_NAME, "aircraftBuyBtn")
        for m in models:
            name = m.find_element(By.XPATH, "../..").text
            for model in cfg["preferred_models"]:
                if model in name:
                    cost_text = m.find_element(By.XPATH, "../../td[4]").text
                    cost = float(cost_text.replace(",", "").replace("$", ""))
                    if cost <= cfg["budget"]:
                        m.click()
                        print(f"🛒 Bought aircraft: {model} for ${cost}")
                        return
        print("🚫 No matching aircraft found within budget.")
    except Exception as e:
        print("❌ Aircraft error:", e)
      
