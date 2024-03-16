from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome Browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

event_widget = driver.find_element(By.CLASS_NAME, "event-widget")
all_events = event_widget.find_elements(By.TAG_NAME, "li")
dict = {}
counter = 0
for event in all_events:
    time = event.find_element(By.TAG_NAME, "time")
    desc = event.find_element(By.TAG_NAME, "a")
    dict[counter] = {"time": time.text, "name": desc.text}
    counter = counter + 1

print(dict)

driver.close()  # Closes the current tab
driver.quit()  # Closes the browser
