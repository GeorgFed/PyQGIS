import processing
resterLyr = QgsRasterLayer("/Users/georg/Downloads/dem/dem.asc", "DEM")
if rasterLyr.isValid():
    QgsProject.instance().addMapLayers([rasterLyr])
    # Параметры для алгоритма
    parameters = {"INPUT": rasterLyr,
                "BAND": 1,
                "INTERVAL": 50.0,
                "FIELD_NAME": "Elv",
                "EXTRA": None,
                "OUTPUT": "/Users/georg/GIS/contours.shp"}
    # Выполняем и отображаем алгоритм
    processing.runAndLoadResults("gdal:contour", parameters)
    