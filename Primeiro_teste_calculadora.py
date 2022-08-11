# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "Android"
caps["appium:deviceName"] = "RX8RA0239TV"
caps["appium:appPackage"] = "com.sec.android.app.popupcalculator"
caps["appium:appActivity"] = "com.sec.android.app.popupcalculator.Calculator"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el6 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="1")
el6.click()
el7 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Mais")
el7.click()
el8 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="1")
el8.click()
el9 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Igual")
el9.click()

# waits 5 seconds

driver.quit()
