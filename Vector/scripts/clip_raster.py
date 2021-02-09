import processing
# Задаем параметры : INPUT - входной растровый файл, MASK - векторная маска, OUTPUT - выходные данные
param = {   'INPUT':'/Users/georg/Desktop/Материалы/SatImage.tif',
            'MASK': '/Users/georg/Downloads/hancock/hancock.shp',
            'SOURCE_CRS': 'srs',
            'TARGET_CRS': 'srs',
            'OUTPUT': '/Users/georg/GIS/clipped.tif'}
# Запускаем алгоритм с параметрами
processing.run("gdal:cliprasterbymasklayer", param)