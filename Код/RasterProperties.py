rasterLyr = QgsRasterLayer("/Users/georg/Downloads/SatImage/SatImage.tif", "SatImage")
if rasterLyr.isValid():
    QgsProject.instance().addMapLayers([rasterLyr])
    # Получаем длину и ширину одного пикселя
    print(rasterLyr.rasterUnitsPerPixelX())
    print(rasterLyr.rasterUnitsPerPixelY())
    # Получаем длину и ширину изображения
    print(rasterLyr.width())
    print(rasterLyr.height())
    # Получаем количество цветовых каналов изображения
    print(rasterLyr.bandCount())