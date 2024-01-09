from bing_image_downloader.downloader import download
import os

# Lista de consultas
queries = ["BANDA ELEVADOR DE BURBUJA DE 3400 X 300 L-202","BANDA DENTADA 192-3M-9MM","BANDA DENTADA 168-2M-9MM","BANDA DENTADA 300-3M-9MM","BANDA DENTADA 187 L 050","BANDA DENTADA 350 5M 09","BANDA DENTADA 1080 T10 25","BANDA DENTADA 305 T5 15","BANDA DENTADA 252 3M 06","BANDA DENTADA 560 T5 15","BANDA DENTADA T10 1560 25","BANDA DENTADA 1720 AT 10 32","Banda dentada 150 XL 15","Banda dentada 825 AT5 15","T5 455x15","BANDA MOD. BELT FX ELASTIC W L628 B120T0.6 LS NO.24133694 METTLER TOLEDO","BANDA JASON 480 - T2.5-7 (BINASA)","BANDA DENTADA 250 S2M 06","BANDA DENTADA 680 T10 15","BANDA DENTADA AT10 1400 25","Banda dentada T10 730 25","Banda dentada 720 T5 15","Banda dentada 285 L 050","Banda dentada 1750-T10-25 MM","BANDA T10 1700 X 30","BANDA DENTADA 810 T10 15","BANDA DENTADA GATES 660 T10 25","BANDA PLANA FIBRAS DE CARBON 2 CAPAS 2190 X 40MM PVC-PEE215BB","BANDA DENTADA 130 XL 037 CX 1","BANDA DENTADA 780 AT5 10","BANDA DENTADA T10 720 25","BANDA 150L050","645-5M BANDA DENTADA","BANDA DENTADA 1040 8MGT 30","Banda dentada T10 660 15","Banda dentada 480 DL 075","BANDA 384 3M 9MM","Banda dentada T5 305 20","Banda dentada 3M 318 09","Banda dentada T10 1960 25","BANDA DENTADA 540 H 100","BANDA DENTADA 750 H 100","BANDA DENTADA 1100 T5 DL 16 DOBLE DENTADO","BANDA DENTADA 455 T5 10","BANDA DENTADA 1720 AT10 35","BANDA DENTADA 500 AT5 15","BANDA DENTADA 420 AT5 15","Banda dentada T10 440 X 20 mm","BANDA DENTADA 390 T5 25","BANDA DENTADA 295 T5 16","BANDA A30","Banda dentada T5 375 25","BANDA DENTADA 700H-100","Banda dentada 780 T10 15","BANDA DENTADA 420 T5 25","BANDA DENTADA T10 DL 1880 25","BANDA DE TIEMPO T10 1250 15 DOBLE CARA","Banda dentada AT10 700 30","BANDA DENTADA 810 T10 12","BANDA T5 420 x 15","Banda dentada 440 T10 25","BANDA 255 L 050 PIRELLI","BANDA DENTADA 1420 5M 09","BANDA DENTADA 360 H 300  CY  2","Banda dentada 450 T5 15","Rodamiento HF 1816","BANDA DENTADA 390 T5 12","BANDA DENTADA T5-4250-30 S WHT 4 MM YELLOW HD GATES","BANDA DENTADA 2000 AT10 30","BANDA AT10 1010-15MM S F","BANDA JASON DOBLE DENTADO 255DL 050","BANDA T10-1250-15 DOBLE DENTADO optibelt","Banda dentada AT10 1400 32","BANDA DENTADA 410 T10 25","BANDA DENTADA 156 XL 037 CY  2","BANDA DENTADA 220 XL 037  CX  1","BANDA T10-880-15","Banda dentada 190 XL 037","BANDA NERY 370 T10 25","BANDA DENTADA 390L50","Banda dentada 1225 T5 16","Banda dentada 420 AT5 10","Banda 180XL X 058","1680 X 15 T10 BANDA S WHT GATES","BANDA AT5-390-25","BANDA DENTADA 1080 T10 15","Banda dentada 5M 535 09","Banda dentada 180 XL 050","Banda dentada 339 3M 037","AT5-660-25 OPTIBEL BANDA","BANDA DENTADA 375 AT5 16","Banda dentada 475 5M 15","Banda dentada AT5 375 20","Banda dentada 450 T10 20","Banda dentada 240L 037","Banda dentada 4160 T5 25","BANDA DENTADA AT-10-780-15","BANDA DENTADA 455 T5 25","BANDA DENTADA 1125 5M 10","BANDA DENTADA 1955 T5 70","3M 252 09 BANDA DENTADA","Banda dentada T5 1955 72","810-AT5-16 GATES BANDA","HTD5-645-15 GATES BANDA","BANDA TP 1000 H100 MCA. GATES COD. 0405-3574","BANDA DENTADA 263L050 MCA. GATES","BANDA DENTADA 520 5M 15MM","BANDA 25.4 T1 2 PULG 2743.2V CON 36 PERFORACIONES PARA INSERTO","BANDA BASCULA METTLER TOLEDO RX2 24110777 560 X 150","BANDA DENTADA T10- 1700-25","BANDA DENTADA 440 T10 30","BANDA DENTADA 180 XL 037","BANDA DENTADA 240 DL 050 DOBLE DENTADO","BANDA DENTADA 322 L 037","BANDA DENTADA 390 H 200","BANDA DENTADA T5 390 OPTIBELT","BANTA DE TRANSMISION A52","BANDA DENTADA 240 L 075 OPTIBELT","BANDA A38","BANDA DE TRANSMISION BX35","BANDA AT10-1080-25 GATES","BANDA DD TP 240 L050 GATES","BANDA UCL218CB 1630X100 ANCHO SIN F","BANDA T5-420-30 JASON","BANDA LISA FIBRAS DE CARBON DE 5300 X 80 MM L161","BANDA DENTADA 440 T10 15","BANDA DENTADA 152 MXL 025","BANDA DENTADA 140 XL 037 OPTIBELT","BANDA DENTADA 130 XL 050 CX 1","Banda dentada 90 XL 037","BANDA DENTADA 420 L 050","Banda dentada 255 L 075","Banda dentada T5 300 15","Banda dentada 710 5M 09","Banda dentada 1880 T10 25","Banda dentada 3048 8M 30","Banda dentada 2400 8M 050","Banda dentada 100 XL 037","BANDA DENTADA 300 XL 19","BANDA DENTADA 1960 T10 15","BANDA ELEVADOR DE BURBUJA DE 3400 X 300 L-202","BANDA DENTADA 192-3M-9MM","BANDA DENTADA 168-2M-9MM","BANDA DENTADA 300-3M-9MM","BANDA DENTADA 187 L 050","T5 455x15","BANDA JASON 480 - T2.5-7 (BINASA)","BANDA DENTADA AT10 1400 25","Banda dentada T10 730 25","Banda dentada 1750-T10-25 MM","BANDA DENTADA 130 XL 037-CX-1","BANDA DENTADA T10 720 25","BANDA DENTADA 1040 8MGT 30","Banda dentada T5 305 20","Banda dentada 3M 318 09","BANDA DENTADA 750 H 100","BANDA DENTADA 1100 T5 DL 16 DOBLE DENTADO","BANDA DENTADA 1720 AT10 35","BANDA DENTADA 500 AT5 15","BANDA DENTADA 420 AT5 15","Banda dentada T10 440 X 20 mm","BANDA DENTADA 390 T5 25","BANDA DENTADA 295 T5 16","BANDA A30","Banda dentada T5 375 25","BANDA DENTADA 700H-100","Banda dentada 780 T10 15","BANDA DENTADA 420 T5 25","BANDA DENTADA T10 DL 1880 25","BANDA DE TIEMPO T10 1250 15 DOBLE CARA","Banda dentada AT10 700 30","BANDA DENTADA 810 T10 12","BANDA T5 420 x 15","Banda dentada 440 T10 25","BANDA 255 L 050 PIRELLI","BANDA DENTADA 1420 5M 09","BANDA DENTADA 360 H 300  CY  2","Banda dentada 450 T5 15","Rodamiento HF 1816","BANDA DENTADA 390 T5 12","BANDA DENTADA T5-4250-30 S WHT + 4 MM YELLOW HD GATES","BANDA DENTADA 2000 AT10 30","BANDA JASON DOBLE DENTADO 255DL 050","BANDA T10-1250-15 DOBLE DENTADO optibelt","Banda dentada AT10 1400 32","BANDA DENTADA 410 T10 25","BANDA DENTADA 156 XL 037 CY 2","BANDA DENTADA 220 XL 037 CX 1","BANDA T10-880-15","Banda dentada 190 XL 037","BANDA NERY 370 T10 25","BANDA DENTADA 390L50","Banda dentada 1225 T5 16","Banda dentada 420 AT5 10","Banda 180XL X 058","1680 X 15 T10 BANDA S WHT GATES","BANDA AT5-390-25","BANDA DENTADA 1080 T10 15","Banda dentada 5M 535 09","Banda dentada 180 XL 050","Banda dentada 339 3M 037","AT5-660-25 OPTIBEL BANDA","BANDA DENTADA 375 AT5 16","Banda dentada 475 5M 15","Banda dentada AT5 375 20","Banda dentada 450 T10 20","Banda dentada 240L 037","Banda dentada 4160 T5 25","BANDA DENTADA AT-10-780-15","BANDA DENTADA 455 T5 25","BANDA DENTADA 1955 T5 70","3M 252 09 BANDA DENTADA","BANDA BASCULA METTLER TOLEDO RX2 24110777 560 X 150","BANDA DENTADA 180 XL 037","BANDA DENTADA 240 DL 050 DOBLE DENTADO","BANDA DENTADA 322 L 037","BANDA DENTADA 390 H 200","BANTA DE TRANSMISION A52","BANDA A38","BANDA DE TRANSMISION BX35","BANDA DD TP 240 L050 GATES","T10-440-30.BANDA DENTADA","BELT T5 305 X25MM","T10 500 15 BANDA","BANDA DENTADA T5 1955 456","BANDA LISA 4L300-B BROUNING","BANDA DE TRANSMISION A52","BANDA DENTADA 210 L 100","BANDA DENTADA 480 L 050","BANDA TRASPORTADORA 190 X 600 MM","BANDA DE TRANSMISION A39","BANDA LISA 2070X160","BANDA LISA 1120 X 75","BANDA LISA 2760 X 100","BANDA VERDE 1260X60 BANDA VERDE LISA","BANDA 880X100","BANDA A38 13X965 LI","2320 X 185 BANDA LISA","BANDA 4360X85","BANDA LISA 10300 X 100","BANDA LISA 3700 X 12","BANDA DENTADA 720-8M U 08","BANDA LISA 1652 X 100","BANDA DENTADA 1130 AT10 25","BANDA LISA 170 X 10","BANDA LISA 2200 X 25 LYNATEX ROJO","BANDA LISA 1130 X 210 FIBRAS DE CARBON","BANDA 2210X25","BANDA 590 X 50 MM","BANDA 2508X40","BANDA DENTADA 1480 AT5 25","BANDA 910 X 200 MM","BANDA LATERAL ESTUCHADORA 690X50","BANDA DENTADA 210 DL 050 DOBLE DENTADO","BANDA T5-500-13MM.","BANDA 4350X 190 MM EM6 200 02PU AZUL","BANDA DENTADA 1900 X 7 CON EMPUJADOR","BANDA LISA 1750 X 200 AZUL","BANDA LISA 1730 X 60 AZUL","BANDA DENTADA 2250 T5 16","BANDA LISA 880 X 160","BANDA T5 300 X 20 MM","BANDA DE ARRASTRE AZUL RIGIDA 3650 X 250","BANDA DE ARRASTRE 1490 X 50","BANDA DE ARRASTRE DE FIBRAS DE CARBONO 1630 X100","BANDA LISA 6004 X 70 FIBRAS DE CARBON","BANDA DENTADA 305 T5 15","BANDA PLANA DE ARRASTRE 740 X 50","BANDA DENTADA 2120 AT10 25","BANDA LISA 5090 X 70 CON CONTORNO DE ESPONJA","1240 X 12 BANDA PLANA DE ARRASTRE GRUESA","BANDA DENTADA 280 T5 25","BANDA LISA DE ARRASTRE RIGIDA 3050 X 15","BANDA LISA DE ARRASTRE RIGIDA 1285 X 100","BANDA DENTADA 3360 14M 55","BANDA DENTADA 420 H 300 CON RECUBRIMIENTO 0.125","BANDA DENTADA AT10 BAUS 1240 X 100 RECUBRIMIENTO RIGIDO EXT","BANDA LISA DE ARRASTRE ENG 2535 X 490","BANDA DENTADA 1960 AT10 32","BANDA LYNATEX ROJO 1060 X 37 CON GUIA V","BANDA EN V LISA SPA 732","BANDA DE TRANSMISION B33","BANDA LISA 3250 X 90 CON RECUBRIMIENTO","BANDA LISA 54 X 1830 CON GUIA","BANDA DE ARRASTRE DE 1210 X 240 MM EM 82 00 02 PU SF","BANDA LISA 2320 X 18 AZUL","TENSOR P BANDA PRINCIPAL NERY","BANDA LISA","POLEA 30L050","POLEA DENTADA 2CGA-50061-22 L501","BANDA DOBLE DENTADO 450 L 050","T2 540 X 8 BANDA","BANDA DENTADA 130 2MGT GT3 5MM","BANDA LISA 6965 X 40 FIBRA DE CARBON","BANDA 3400 X 45 PERFORADA FIBRAS DE CARBON","BANDA LISA 2540 X 450 AZUL","BANDA LISA 1920 X 570 FIBRA DE CARBON","BANDA LISA 3950 X 400 FIBRAS DE CARBON","BANDA LINARAN 1240X60 LISA RPG-10","T10 530 X 20 BANDA DENTADA","BANDA 775 X 50 MM SUPER GRIP VERDE","BANDA DE PLANCHADO DE ETIQUETA 775 X 120 MM L-400","BANDA 4000 X 100 MM FIBRAS DE CARBON","BANDA VERDE 2100X30","BANDA DE ARRATRE 2200X30 L400","BANDA 255-5M-50","BANDA 650X120","BANDA PERFORADA DE 2720 X 35 MM DE FIBRA DE CARBONO","5M-800-9 BANDA","BANDA LISA VERDE 6330 X 150 MM","BANDA DENTADA 430 AT5 10","BANDA DENTADA T5 375 16","BANDA T5 295 20","BANDA 3048-8M-50","BANDA LISA 1225X15MM","BANDA B102 GATES","BANDA T10 1690 X 15 MM","BANDA LISTA 1255 X 15 VERDE","BANDA PERFORADA 2700 X 40 FIBRAS DE CARBON","BANDA 14M-1232-28 GUIA CENTRAL 7 32 PULG Y BARRENOS 1 8 PULG C 44 DI","BANDA ELEVADOR DE TAPA 3240 X 300 MM S FC EMP C 17 EMPUJADOR","BANDA PLANA 2300 X 250 MM C GUIA AL CENTRO EM6 2 00 015 PU S","BANDA DENTADA 15X645 PASO 5HTD645-5M-15 POGGI1520293089","BANDA PGN220CB (70 X 2630 MM)","BANDA FIBRA DE CARBON 2320 X 40 MM S F","BANDA PLANA DE 3120 X 250 MM S F","BANDA DE ARRASTRE 3280 X 80","BANDA FIBRAS DE CARBON 6500X40MM","BANDA EN V NARANJA VO-13-AB3-A","BANDA CIRCULAR NARANJA 8MM AB RO-08","POLEA PARA BANDA DE SALIDA ETIQUETADORA NERY L-104 106 107","POLEAS DENTADAS P  SISTEMA DE TRACCION","BANDA PLANA SIN FIN RUGOSA CON GUIA PARA TAPADORA L-404 312","360 H X 300 BANDA PARA PLANCHADO","BANDA 1422V360","MOTOR DE BANDA DE ARRASTRE ETIQUETADORA 51K100VEST2-GHR10","BANDA TRANSMISION B-60 BLACK GOLD","BANDA DENTADA JASON T5-1755-16","POLEA PILEGGIA 1PB0583790","BANDA CON RECUBRIMIENTO DE ESPONJA 1060 X 37","3650 X 230 MM S-F BANDA FIBRAS DE CARBON","BANDA GATES 800H100","BANDA DENTADA 900H-100 C RECUBRIMIENTO ROJO DE 10MM","BANDA DE TRANSMISION 1915X30 MM GGS09.30","BANDA DE ARRASTRE 370X12 L215 ETIQ. GARANTIA","BANDA FIBRA CARBON 6570 X 220","250-2MGT-06-GT3- GATES BANDA","BANDA DENTADA PORTATUBOS IWKA PARA L-310, L-312 2072293","BANDA 2120X100","BANDA DENTADA 152 MXL 025","BANDA DENTADA 130 XL 050 CX  1","Banda dentada 90 XL 037","BANDA DENTADA 420 L 050","Banda dentada 255 L 075","Banda dentada T5 300 15","Banda dentada 710 5M 09","Banda dentada 1880 T10 25","Banda dentada 3048 8M 30","Banda dentada 2400 8M 050","Banda dentada 100 XL 037","BANDA DENTADA 300 XL 19","BANDA DENTADA 1960 T10 15"]

# Carpeta de salida común para todas las consultas
output_base_folder = 'U:\Imagenes Loreal SLP\BANDAS-DE-LINEA'

# Configuración común para todas las consultas
common_settings = {
    'limit': 5,
    'adult_filter_off': True,
    'force_replace': False,
    'timeout': 60,
    'filter': "photo",
    'verbose': True
}



# Iterar sobre cada consulta y descargar imágenes
for query in queries:
    print(f'Descargando imágenes para la consulta: {query}')
    
    # Crear una carpeta para la consulta actual dentro de la carpeta base
    query_folder = os.path.join(output_base_folder)
    os.makedirs(query_folder, exist_ok=True)
    
    # Establecer la carpeta de salida en las configuraciones comunes
    common_settings['output_dir'] = query_folder
    
    # Ejecutar la descarga
    download(query, **common_settings)

print('Descarga completa para todas las consultas.')