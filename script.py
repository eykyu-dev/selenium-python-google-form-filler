from selenium import webdriver
from selenium.webdriver.common.by import By

# Open the web page
driver = webdriver.Chrome()

email = driver.find_element("css selector", '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div:nth-child(1) > div.rFrNMe.k3kHxc.RdH0ib.yqQS1.zKHdkd > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
email.send_keys("dwadaw")

first_last = driver.find_element("css selector", '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
first_last.send_keys("dawdwa")

providing_table = driver.find_element("css selector", '#i13 > div.vd3tt > div')
providing_table.click()

artist_name = driver.find_element("css selector", '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(4) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
artist_name.send_keys("@dwad")

phone_num = driver.find_element("css selector", '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(5) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
phone_num.send_keys("adw-wdadw-daw")

selling = driver.find_element("css selector", '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(9) > div > div > div.AgroKb > div > div.RpC4Ne.oJeWuf > div.Pc9Gce.Wic03c > textarea')
selling.send_keys("adw, daw, awd, daw")

agree = driver.find_element("css selector", '#i93 > div.uHMk6b.fsHoPb')
agree.click()

driver.close()
