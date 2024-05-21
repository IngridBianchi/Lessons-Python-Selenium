from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from concurrent.futures import ThreadPoolExecutor

def run_test(test_number):
    try:
        # Configuro las opciones del navegador para ejecutar headless
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(options=chrome_options)

        # Cargp la página web
        driver.get("https://demoqa.com/broken")

        # Busco la imagen broken
        try:
            image_element_broken = driver.find_element(By.XPATH, "//IMG[@src='/images/Toolsqa_1.jpg']")
            if image_element_broken.is_displayed():
                print(f"Prueba {test_number}: La imagen broken está visible.")
            else:
                print(f"Prueba {test_number}: La imagen broken no está visible.")
        except NoSuchElementException:
            print(f"Prueba {test_number}: No se encontró la imagen broken.")

        # Busco la imagen normal
        try:
            image_element = driver.find_element(By.XPATH, "(//IMG[@src='/images/Toolsqa.jpg'])[2]")
            if image_element.is_displayed():
                print(f"Prueba {test_number}: La imagen está visible.")
            else:
                print(f"Prueba {test_number}: La imagen no está visible.")
        except NoSuchElementException:
            print(f"Prueba {test_number}: No se encontró la imagen.")

        # Cierro el navegador
        driver.quit()
    except Exception as e:
        print(f"Error en la prueba {test_number}: {e}")

# Nro de instancias que quiero ejecutar en paralelo
num_instances = 5

# Uso ThreadPoolExecutor para ejecutar pruebas en paralelo
with ThreadPoolExecutor(max_workers=num_instances) as executor:
    executor.map(run_test, range(num_instances))
