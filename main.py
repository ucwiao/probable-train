import schedule, time
from actions import login, fuel, flights, aircraft

def run_bot():
    print("🔁 Running AM4 bot cycle...")
    driver = login.get_driver()

    if login.login(driver):
        fuel.auto_fuel(driver)
        flights.auto_schedule(driver)
        aircraft.auto_buy_aircraft(driver)
    else:
        print("❌ Login failed")

    driver.quit()

def get_interval():
    import json
    with open("config/schedule_config.json") as f:
        return int(json.load(f)["interval_minutes"])

# Run once immediately
run_bot()

# Then repeat every X minutes
schedule.every(get_interval()).minutes.do(run_bot)
print("🕒 Bot started. Waiting for next run...")

while True:
    schedule.run_pending()
    time.sleep(1)
  
