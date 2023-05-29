from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import numpy as np
import pandas as pd

input ="asus 1650 ekran kartı"

driver = webdriver.Chrome()
driver.maximize_window()








"""
#--Trendyol--
driver.get("https://www.trendyol.com/butik/liste/1/kadin")
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"V8wbcUhU")))
search_bar_trendyol = driver.find_element(By.CLASS_NAME,"V8wbcUhU")
search_bar_trendyol.send_keys(input)

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"cyrzo7gC")))
search_button_trendyol = driver.find_element(By.CLASS_NAME, "cyrzo7gC")
search_button_trendyol.click()

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"prdct-desc-cntnr-name")))
item_name_trendyol = driver.find_elements(By.CLASS_NAME, "prdct-desc-cntnr-name")

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"prc-box-dscntd")))
item_price_trendyol = driver.find_elements(By.CLASS_NAME, "prc-box-dscntd")

trenyol_name_list = []
trenyol_price_list = []

for trenyol_name in item_name_trendyol:
    trenyol_name_list.append(trenyol_name.text)

for trenyol_price in item_price_trendyol:
    trenyol_price_list.append(trenyol_price.text)

print(trenyol_price_list)
print(trenyol_name_list)

df_trendyol = pd.DataFrame({'website':"Tredyol",'Item Name':trenyol_name_list,'Item Price': trenyol_price_list })

print(df_trendyol)
"""

"""
#--HEPSİBURADA--

driver.get("https://www.hepsiburada.com/")
WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"theme-IYtZzqYPto8PhOx3ku3c")))
search_bar = driver.find_element(By.CLASS_NAME, "theme-IYtZzqYPto8PhOx3ku3c")
search_bar.send_keys(input)

WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"searchBoxOld-yDJzsIfi_S5gVgoapx6f")))
search_button = driver.find_element(By.CLASS_NAME, "searchBoxOld-yDJzsIfi_S5gVgoapx6f")
search_button.click()

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "horizontalSortingBar-Ce404X9mUYVCRa5bjV4D")))
sorting_area = driver.find_element(By.CLASS_NAME, "horizontalSortingBar-Ce404X9mUYVCRa5bjV4D")
sorting_area.click()

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "horizontalSortingBar-wxPx75gvwcKxOM8rMngA")))
Lower_price_area = driver.find_element(By.CLASS_NAME, "horizontalSortingBar-wxPx75gvwcKxOM8rMngA")
Lower_price_area.click()
time.sleep(4)

items_name = driver.find_elements(By.CSS_SELECTOR, "h3[data-test-id='product-card-name']")
time.sleep(2)
items_price = driver.find_elements(By.CSS_SELECTOR, "div[data-test-id='price-current-price']")

hepsi_name_list = []
hepsi_price_list = []
for item_name in items_name:
    hepsi_name_list.append(item_name.text)

for item_price in items_price:
    hepsi_price_list.append(item_price.text)

df_test = pd.DataFrame({'website':"hepsiburada",'Item Name':hepsi_name_list,'Item Price': hepsi_price_list })

print(df_test)
"""


while True:
    continue