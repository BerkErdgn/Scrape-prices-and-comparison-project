from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#time.sleep() kullanmak antıklı değil Bu yüzden aşağıdakileri kullanıyoruz.
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

input ="asus 1650 ekran kartı"

driver = webdriver.Chrome()
driver.maximize_window()

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


for item_name in items_name:
    print("**************************")
    print(item_name.text)

for item_price in items_price:
    print("**************************")
    print(item_price.text)



while True:
    continue