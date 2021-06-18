from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

driver = webdriver.Chrome()

driver.get("http://www.example.com")
time.sleep(10)
driver.close()
