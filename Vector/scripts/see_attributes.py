layer = QgsVectorLayer("D:/hse/GIS/qgis_vector/nyc/NYC_MUSEUMS_GEO.shp", "New York City Museums", "ogr")
# Получаем итератор по свойствам слоя
features = layer.getFeatures()
# Проходим по итератору и отображаем свойства
f = feature.__next__()
f.attributes()
