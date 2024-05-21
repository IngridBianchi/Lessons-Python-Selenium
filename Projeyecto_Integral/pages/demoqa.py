from abc import ABC, abstractmethod
from src.cliente import Cliente
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
import pytest



class AbstractPageTest(ABC):
    url = None
    cliente = None

    def __init__(self, cliente: Cliente):
        self.cliente = cliente

    @abstractmethod
    def testear(self, cliente):
        pass


class DemoqaAutomationPracticeForm(AbstractPageTest):
  def testear(self):
    self.url = "https://demoqa.com/automation-practice-form"
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(self.url)
        actions = ActionChains(driver)

        for key, value in self.cliente.items_datos_personales():
            if key == "subjects":
                element = driver.find_element(By.XPATH, f"//INPUT[@id='subjectsInput']")
                for subject in value:
                    element.send_keys(subject)
                    element.send_keys(Keys.ENTER)
                element.send_keys(value)
            elif key == "hobbies":
                for hobbie in value:
                    element = driver.find_element(By.XPATH, f"//LABEL[@title=''][text()='{hobbie}']")
                    # element.click()
            elif key == "gender":
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                wait = WebDriverWait(driver, 10)
                element = driver.find_element(By.XPATH, f"//LABEL[@title=''][text()='{value}']")
                element.click()
            elif key == "state":
                # pass
                select_element = driver.find_element(By.XPATH, "//input[@id='react-select-3-input']")
                # select_element = Select(driver.find_element(By.XPATH, "//DIV[@class=' css-1wa3eu0-placeholder'][text()='Select State']"))
                # element = driver.find_element(By.XPATH, "//input[@id='react-select-3-input']")
                select_element.send_keys(value)
                # select_element.select_by_value(value)
            elif key == "city":
                pass
                # select_element = Select(driver.find_element(By.XPATH, "(//DIV[@class='col-md-4 col-sm-12'])[2]"))
                # select_element.select_by_value(value)
                # element = driver.find_element(By.XPATH, "//input[@id='react-select-4-input']")
                # element.clear()
                # element.send_keys(value)
            # elif key == "dateOfBirthInput":
            #     element = driver.find_element(By.XPATH, f"//INPUT[@id='{key}']")
            #     element.click()
            #     parts = value.split()
            #     year = driver.find_element(By.XPATH, "//SELECT[@class='react-datepicker__year-select']")
            #     select_year = Select(year)
            #     select_year.select_by_value(parts[2])

            #     month = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//SELECT[@class='react-datepicker__month-select']")))
            #     select_month = Select(month)
            #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//option[text()='July']")))
            #     select_month.select_by_visible_text(parts[1])

            #     day = int(parts[0])
            #     elemento_dia = driver.find_element(By.XPATH, f"//DIV[@class='react-datepicker__day react-datepicker__day--0{parts[0]} react-datepicker__day--selected'][text()='{day}']")
            #     elemento_dia.click()
            else:
                element = driver.find_element(By.XPATH, f"//INPUT[@id='{key}']")
                element.clear()
                element.send_keys(value)

        for domicilio in self.cliente.items_domicilios():
            domicilio_dict = dict(domicilio)
            if domicilio_dict['is_shipping']:
                element = driver.find_element(By.XPATH, "//TEXTAREA[@id='currentAddress']")
                element.clear()
                element.send_keys(domicilio_dict['adress'])

    except Exception as e:
        pytest.fail(f"Error en DemoqaAutomationPracticeForm: {e}")

    finally:
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(5)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.invisibility_of_element_located((By.XPATH, "//iframe[@id='google_ads_iframe_']")))
        # close_button = driver.find_element(By.XPATH,"//BUTTON[@id='closeLargeModal']")
        # close_button.click()
        # actions.send_keys(Keys.ESCAPE).perform()
        driver.quit()

class DemoqaTextBox(AbstractPageTest):
  def testear(self):
    self.url = "https://demoqa.com/text-box"
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(self.url)

        for key, value in self.cliente.items_datos_personales():
            if key == "lastName":
                element = driver.find_element(By.XPATH, f"//INPUT[@id='userName']")
                element.send_keys(self.cliente.get_fullName())
            elif key == "userEmail":
                element = driver.find_element(By.XPATH, f"//INPUT[@id='userEmail']")
                element.send_keys(value)
            else:
                pass

        for domicilio in self.cliente.items_domicilios():
            domicilio_dict = dict(domicilio)
            if domicilio_dict['is_shipping']:
                element = driver.find_element(By.XPATH, "//TEXTAREA[@id='currentAddress']")
                element.clear()
                element.send_keys(domicilio_dict['adress'])
            else:
                element = driver.find_element(By.XPATH, "//TEXTAREA[@id='permanentAddress']")
                element.clear()
                element.send_keys(domicilio_dict['adress'])

    except Exception as e:
        pytest.fail(f"Error en DemoqaTextBox: {e}")
    finally:
        time.sleep(10)
        driver.quit()