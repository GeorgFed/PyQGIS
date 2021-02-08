lyr = QgsVectorLayer("D:/hse/GIS/project_qgis_repository/PyQGIS/Vector/scripts/nyc/NYC_MUSEUMS_GEO.shp", "Museums", "ogr")
fts = lyr.getFeatures()
# Получаем первый объект
first = fts.__next__()
# Получаем последний объект 
last = fts.__next__()
for f in fts:
  last = f
# Измеряем дистанцию в градусах
d = QgsDistanceArea()
m = d.measureLine(first.geometry().asPoint(), last.geometry().asPoint())
# Переводим дистанцию в метры
print(d.convertLengthMeasurement(m, 0))
# Результат: 4401.162
