import processing
rasterLyr = QgsRasterLayer("/Users/georg/Downloads/SatImage/SatImage.tif", "Resolution")
if rasterLyr.isValid():
    # Нужно получить информацию о проекции изображения
    epsg = rasterLyr.crs().postgisSrid()
    srars = 'EPSG: %s' % epsg
    # Берем изначальный размер пикселя и увеличиваем на 2 - так мы сожмем изображение
    res =  rasterLyr.rasterUnitsPerPixelX() * 2
    # Задаем параметры
    params = {  'INPUT': rasterLyr,
                'TARGET_CRS': 'srs',
                'TARGET_EXTENT_CRS': 'srs',
                'TARGET_RESOLUTION': res,
                'RESAMPLING': 0,
                'OPTIONS': None, 
                'DATA_TYPE': 0,
                'OUTPUT': '/Users/georg/GIS/resampled.tif'}
    # Проводим алгоритм и отображаем результат
    processing.run('gdal:warpreproject', params)