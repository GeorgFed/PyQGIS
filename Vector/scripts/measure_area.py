# Создаем слой
layer = QgsVectorLayer("D:/hse/GIS/project_qgis_repository/PyQGIS/Vector/scripts/ms/mississippi.shp", "Missisipi", "ogr")
# Отображаем слой
QgsProject.instance().addMapLayers([layer])
# Получаем объекты на слое
fts = layer.getFeatures()
# Получаем первый объект из итератора
boundary = fts.__next__()
# иницилизируем конвертатор
d = QgsDistanceArea()
# Конвертируем из градусов в мили
print(d.convertAreaMeasurement(boundary.geometry().area(), 7))