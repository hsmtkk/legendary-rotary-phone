from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

MY_PROXY = "proxy.iiji.jp:8080"
prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = MY_PROXY
prox.ssl_proxy = MY_PROXY

capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)
driver = webdriver.Chrome(desired_capabilities=capabilities)

driver.get("http://www.example.com")
time.sleep(10)
driver.close()
