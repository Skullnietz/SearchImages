import gspread
from google.oauth2.service_account import Credentials
from gspread_formatting import format_cell_range, Color

# Load credentials from a JSON file
creds = Credentials.from_service_account_file("ruta/a/tu/credencial.json", scopes=["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"])

# Create a client connection
client = gspread.authorize(creds)

# Open the spreadsheet (make sure to share the sheet with the email in the JSON credentials)
hoja_nombre = "NombreDeTuHoja"
spreadsheet = client.open(hoja_nombre)
hoja = spreadsheet.sheet1  # Assuming it's the first sheet, you can adjust as needed

# Two example lists
lista1 = ["BANDA HORIZONTAL", "BANDA DENTADA", "OTRA CARPETA", "CARPETA COMUN"]

# Get the range of cells containing the list in a cell (for example, A1)
rango_celdas = hoja.get("A1")

# Get the value of the cell and split the text into a list
contenido_celda = rango_celdas[0][0].value.split("\n")

# Iterate through the cells and compare with lista1
for i, valor in enumerate(contenido_celda):
    if valor in lista1:
        # Mark the cell in green if it's in lista1
        hoja.update(f'B{i+1}', value=valor)
        formato = dict(backgroundColor=Color(0, 1, 0, 0))  # Green color
        format_cell_range(hoja, f'B{i+1}', formato)
    else:
        # Mark the cell in red if it's not in lista1
        hoja.update(f'B{i+1}', value=valor)
        formato = dict(backgroundColor=Color(1, 0, 0, 0))  # Red color
        format_cell_range(hoja, f'B{i+1}', formato)

# Save the changes to the spreadsheet
hoja.update('A1', value='\n'.join(lista1))
