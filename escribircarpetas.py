import os

# Ruta de la carpeta que quieres explorar
ruta_carpeta = "U:\Imagenes Loreal SLP\BANDAS-DE-LINEA"

# Lista todas las carpetas en la ruta especificada
carpetas = [nombre for nombre in os.listdir(ruta_carpeta) if os.path.isdir(os.path.join(ruta_carpeta, nombre))]

# Ruta del archivo de texto donde se almacenarán los nombres de las carpetas
ruta_archivo = "nombres_carpetas.txt"

# Abre el archivo en modo escritura
with open(ruta_archivo, 'w') as archivo:
    # Escribe los nombres de las carpetas en el archivo, separados por comas y entre comillas
    for carpeta in carpetas:
        archivo.write(f'"{carpeta}",')

# Imprime un mensaje indicando que se ha completado el proceso
print(f'Se han listado las carpetas en el archivo: {ruta_archivo}')