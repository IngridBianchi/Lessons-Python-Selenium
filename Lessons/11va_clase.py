from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

driver.get("https://demoqa.com/broken")

try:
    image_element_broken = driver.find_element(By.XPATH, "//IMG[@src='/images/Toolsqa_1.jpg']")
    if image_element_broken.is_displayed():
        print("La imagen broken está visible.")
    else:
        print("La imagen broken no está visible.")
except NoSuchElementException:
    print("No se encontró la imagen broken.")

try:
    image_element = driver.find_element(By.XPATH, "(//IMG[@src='/images/Toolsqa.jpg'])[2]")
    if image_element.is_displayed():
        print("La imagen está visible.")
    else:
        print("La imagen no está visible.")
except NoSuchElementException:
    print("No se encontró la imagen.")

driver.quit()
