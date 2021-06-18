from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

driver = webdriver.Chrome()

driver.get("https://dictionary.cambridge.org/dictionary/english-japanese/")

search_word = driver.find_element_by_id("searchword")
search_word.send_keys("computer")

button = driver.find_element_by_class_name("cdo-search-button")
button.click()

trans = driver.find_element_by_class_name("def")
print(trans.text)

time.sleep(60)

driver.close()
