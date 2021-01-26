# Подключаем библиотеку алгоритмов обработки геоданных
import processing
resterLyr = QgsRasterLayer("/Users/georg/Downloads/dem/dem.asc", "Hillshade")
if rasterLyr.isValid():
    # Передаем параметры генерации тени на местности
    parameters = {'INPUT': rasterLyr, 
                'BAND': 1, # 
                'COMPUTE_EDGES': False,
                'ZEVENBERGEN': False,
                'Z_FACTOR': 1.0,
                'SCALE': 1.0,
                'AZIMUTH': 315,
                'ALTITUDE': 45,
                'OUTPUT': "/Users/georg/GIS/hillshade.tif"}
    # Получаем результат работы алгоритма
    processing.runAndLoadResults("gdal:hillshade", parameters)