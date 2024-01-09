from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def buscar_y_descargar_imagenes(query, cantidad=10):
    # Configura el controlador del navegador (asegúrate de tener el controlador en el PATH del sistema)
    driver = webdriver.Chrome()

    try:
        # Abre el navegador y carga Google Images
        driver.get("https://www.google.com/imghp")

        # Localiza el cuadro de búsqueda
        search_box = driver.find_element("name", "q")

        # Ingresa la consulta de búsqueda
        search_box.send_keys(query)

        # Presiona Enter para realizar la búsqueda
        search_box.send_keys(Keys.RETURN)

        # Espera a que se carguen los resultados de la búsqueda
        time.sleep(2)

        # Itera a través de los resultados y realiza la descarga
        image_links = driver.find_elements(By.CSS_SELECTOR,(".rg_i"))

        for i in range(min(cantidad, len(image_links))):
            # Haz clic en el enlace para abrir la imagen en una nueva pestaña
            image_links[i].click()

            # Espera a que se abra la nueva pestaña
            time.sleep(2)

            # Cambia a la nueva pestaña
            driver.switch_to.window(driver.window_handles[1])

            # Encuentra la imagen completa y guárdala (ajusta según la estructura de la página)
            full_image = driver.find_elements(By.CSS_SELECTOR,(".n3VNCb img"))
            src = full_image.get_attribute("src")
            driver.get(src)
            with open(f"{query}_{i+1}.jpg", "wb") as f:
                f.write(driver.page_source.encode("utf-8"))

            # Cierra la pestaña actual
            driver.close()

            # Vuelve a la pestaña de resultados de búsqueda
            driver.switch_to.window(driver.window_handles[0])

    finally:
        # Cierra el navegador al finalizar
        driver.quit()

# Ejemplo de uso
buscar_y_descargar_imagenes("gatos lindos", cantidad=10)
