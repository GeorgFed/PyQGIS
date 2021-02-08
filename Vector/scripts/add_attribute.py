vectorLyr =  QgsVectorLayer('/Users/georg/Downloads/PyQGIS-main/Vector/scripts/nyc/NYC_MUSEUMS_GEO.shp', 'Museums' , "ogr")
vpr = vectorLyr.dataProvider()
# Создаем геометрию - точку
pnt = QgsGeometry.fromPointXY(QgsPointXY(-74.80,40.549))
fields = vpr.fields()
f = QgsFeature(fields)
# Добавляем геометрию на слой
f.setGeometry(pnt)
# Редактируем свойства - они хранятся в виде упорядоченного словаря
f['NAME'] = 'HSE Museum'
vpr.addFeatures([f])
# Обновляем слой
vectorLyr.updateExtents()
# Отображаем
QgsProject.instance().addMapLayers([vectorLyr])