from selenium import webdriver
PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/")

print(driver.title)

#driver.quit() quits all
#driver.close() closes tab