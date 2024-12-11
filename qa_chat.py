import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# Open the page
driver.get("https://chatgpt.com/")

# Wait for the page to load
time.sleep(5)

# Locate the contenteditable element
search_bar = driver.find_element(By.ID, "prompt-textarea")

# Input data into the contenteditable element using JavaScript
driver.execute_script("arguments[0].innerText = 'GitHub Copilot';", search_bar)

# Simulate pressing the Enter key
search_bar.send_keys(Keys.RETURN)

# Wait for a few seconds to see the results
time.sleep(20)

# Close the browser
driver.quit()