vectorLyr =  QgsVectorLayer('/Users/georg/Downloads/PyQGIS-main/Vector/scripts/nyc/NYC_MUSEUMS_GEO.shp', 'Museums' , "ogr")
vpr = vectorLyr.dataProvider()
# Создаем геометрию - точку
pnt = QgsGeometry.fromPointXY(QgsPointXY(-74.80,40.549))
f = QgsFeature()
# Добавляем геометрию на слой
f.setGeometry(pnt)
vpr.addFeatures([f])
# Обновляем слой
vectorLyr.updateExtents()
# Отображаем
QgsProject.instance().addMapLayers([vectorLyr])