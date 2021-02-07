# Создаем слой
layer = QgsVectorLayer("D:/hse/GIS/qgis_vector/nyc/NYC_MUSEUMS_GEO.shp", "New York City Museums", "ogr")
# Получаем итератор по характеристикам слоя
features = layer.getFeatures()
# Проходим по итератору
f = features.__next__()
g = f.geometry()
# Отображаем геометрию характеристики как точку
print(g.asPoint())
