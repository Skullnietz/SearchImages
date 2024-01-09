from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

def buscar_imagenes_y_guardar(query, cantidad=10, directorio_destino="imagenes"):
    # Configuración del navegador
    driver = webdriver.Chrome()  # Asegúrate de tener el controlador de Chrome instalado y actualizado

    # Navegar a la página de imágenes de Google
    driver.get("https://www.google.com/imghp")

    # Encontrar el cuadro de búsqueda de imágenes
    search_box = driver.find_element("name", "q")

    # Ingresar la consulta y presionar Enter
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    # Esperar un momento para que los resultados se carguen
    time.sleep(2)

    # Desplazarse hacia abajo para cargar más imágenes (puedes ajustar este valor según tus necesidades)
    for _ in range(cantidad // 10):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # Encontrar los elementos de las imágenes
    image_elements = driver.find_elements("css selector", ".rg_i")

    # Crear el directorio de destino si no existe
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)

    # Descargar y guardar las imágenes
    for i, element in enumerate(image_elements):
        image_url = element.get_attribute("src")

        # Descargar la imagen
        image_path = os.path.join(directorio_destino, f"{query}_imagen_{i + 1}.jpg")
        urllib.request.urlretrieve(image_url, image_path)
        print(f"Imagen {i + 1} de '{query}' descargada y guardada en {image_path}")

    # Cerrar el navegador
    driver.quit()

def buscar_imagenes_para_lista(consultas, cantidad=10):
    for consulta in consultas:
        buscar_imagenes_y_guardar(consulta, cantidad)

# Ejemplo de uso con una lista de consultas
consultas = ["gatos ", "perros ", "paisajes "]
buscar_imagenes_para_lista(consultas, cantidad=10)
