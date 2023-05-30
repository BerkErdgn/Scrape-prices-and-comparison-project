from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pandas as pd

input = input("Item Name : ")

driver = webdriver.Chrome()
driver.maximize_window()



#--n11--
driver.get("https://www.n11.com/")
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.ID,"searchData")))
search_bar_n11 = driver.find_element(By.ID,"searchData")
search_bar_n11.send_keys(input)

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"iconsSearch")))
search_button_n11 = driver.find_element(By.CLASS_NAME,"iconsSearch")
search_button_n11.click()

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "productName")))
item_name_n11 = driver.find_elements(By.CLASS_NAME, "productName")

WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "newPrice")))
item_price_n11 = driver.find_elements(By.CLASS_NAME, "newPrice")

n11_name_list = []
n11_price_list = []

for n11_name in item_name_n11:
    n11_name_list.append(n11_name.text)

for n11_price in item_price_n11:
    price_n11 = n11_price.text.replace("TL", "").replace(".","").replace(",",".")
    n11_price_list.append(float(price_n11))

df = pd.DataFrame({'website':"n11",'Item Name':n11_name_list,'Item Price': n11_price_list })


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
    price_ciceksepeti = ciceksepeti_price.text.replace("\n","").replace("TL", "").replace(".", "").replace(",", ".")
    ciceksepeti_price_list.append(float(price_ciceksepeti))

df_ciceksepeti = pd.DataFrame({'website':"ÇiçekSepeti",'Item Name':ciceksepeti_name_list,'Item Price': ciceksepeti_price_list })

df = df._append(df_ciceksepeti, ignore_index=True)

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
    price_trenyol = trenyol_price.text.replace("\n", "").replace("TL", "").replace(".", "").replace(",", ".")
    trenyol_price_list.append(float(price_trenyol))

df_trendyol = pd.DataFrame({'website':"Trendyol",'Item Name':trenyol_name_list,'Item Price': trenyol_price_list })

df = df._append(df_trendyol, ignore_index=True)

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
    price_hepsi = item_price.text.replace("\n", "").replace("TL", "").replace(".", "").replace(",", ".")
    hepsi_price_list.append(float(price_hepsi))

df_hepsiburada = pd.DataFrame({'website':"hepsiburada",'Item Name':hepsi_name_list,'Item Price': hepsi_price_list })

df = df._append(df_hepsiburada, ignore_index=True)


print(df.sort_values("Item Price"))


time.sleep(2)
driver.close()