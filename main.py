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
#--Amazon-- Sorunlu geri dön
driver.get("https://www.amazon.com.tr/")
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"nav-input")))
search_bar_amazon = driver.find_element(By.CLASS_NAME,"nav-input")
search_bar_amazon.send_keys(input)

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.ID,"nav-search-submit-button")))
search_button_amazon = driver.find_element(By.ID,"nav-search-submit-button")
search_button_amazon.click()

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "a-size-base-plus")))
item_name_amazon = driver.find_elements(By.CLASS_NAME, "a-size-base-plus")

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "a-size-base-plus")))
item_price_amazon = driver.find_elements(By.CLASS_NAME, "a-price-whole")

amazon_name_list = []
amazon_price_list = []

for amazon_name in item_name_amazon:
    amazon_name_list.append(amazon_name.text)

for amazon_price in item_price_amazon:
    amazon_price_list.append(amazon_price.text)

print(amazon_name_list)
print(amazon_price_list)
print(len(amazon_price_list))
print(len(amazon_name_list))

df_amazon = pd.DataFrame({'website':"Amazon",'Item Name':amazon_name_list,'Item Price': amazon_price_list })

print(df_amazon)

"""

"""

#--ÇicekSepeti--
driver.get("https://www.ciceksepeti.com/")

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"item-extra")))
entry_button_ciceksepeti = driver.find_element(By.CLASS_NAME,"item-extra")
entry_button_ciceksepeti.click()

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"product-search__input")))
search_bar_ciceksepeti = driver.find_element(By.CLASS_NAME,"product-search__input")
search_bar_ciceksepeti.send_keys(input)

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"icon-search-444")))
search_button_ciceksepeti = driver.find_element(By.CLASS_NAME,"icon-search-444")
search_button_ciceksepeti.click()

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "products__item-title")))
item_name_ciceksepeti = driver.find_elements(By.CLASS_NAME, "products__item-title")

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "price--now")))
item_price_ciceksepeti = driver.find_elements(By.CLASS_NAME, "price--now")

ciceksepeti_name_list = []
ciceksepeti_price_list = []

for ciceksepeti_name in item_name_ciceksepeti:
    ciceksepeti_name_list.append(ciceksepeti_name.text)

for ciceksepeti_price in item_price_ciceksepeti:
    price = ciceksepeti_price.text.replace("\n","")
    ciceksepeti_price_list.append(price)

print(ciceksepeti_name_list)
print(ciceksepeti_price_list)
print(len(ciceksepeti_name_list))
print(len(ciceksepeti_price_list))

df_ciceksepeti = pd.DataFrame({'website':"ÇiçekSepeti",'Item Name':ciceksepeti_name_list,'Item Price': ciceksepeti_price_list })

print(df_ciceksepeti)





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