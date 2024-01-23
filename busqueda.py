from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Lista de términos de búsqueda
search_terms = ["Carro mustang", "Playstation", "PCgamer"]

# Configurar el navegador Chrome (descarga el controlador de Chrome: https://sites.google.com/chromium.org/driver/)
chrome_options = Options()
chrome_options.add_argument('--headless')  # Ejecutar en modo sin cabeza (sin interfaz gráfica)
driver = webdriver.Chrome(options=chrome_options)

for term in search_terms:
    # Construir la URL de búsqueda en Google Images
    search_url = f'https://www.google.com/search?q={term}&tbm=isch'

    # Abrir la URL en el navegador
    driver.get(search_url)
    time.sleep(2)  # Esperar un tiempo para cargar la página (puede ser ajustado según la velocidad de tu conexión)

    # Encontrar el primer elemento de imagen y hacer clic en él
    try:
        first_image = driver.find_element_by_css_selector('img.Q4LuWd')
        first_image.click()
        time.sleep(2)  # Esperar un tiempo para cargar la imagen a tamaño completo
    except Exception as e:
        print(f"No se pudo encontrar la imagen para '{term}': {str(e)}")
        continue

    # Obtener la URL de la imagen a tamaño completo
    try:
        full_size_image_url = driver.find_element_by_css_selector('.n3VNCb img').get_attribute('src')
        print(f"Imagen para '{term}': {full_size_image_url}")
        # Puedes descargar la imagen usando urllib u otra biblioteca de descarga de imágenes aquí
    except Exception as e:
        print(f"No se pudo obtener la URL de la imagen para '{term}': {str(e)}")

# Cerrar el navegador al final
driver.quit()
