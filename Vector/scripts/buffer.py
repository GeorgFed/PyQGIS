# Создаем слой
layer = QgsVectorLayer("D:/hse/GIS/project_qgis_repository/PyQGIS/Vector/scripts/nyc/NYC_MUSEUMS_GEO.shp", "New York City Museums", "ogr")
# Отображаем слой
QgsProject.instance().addMapLayers([layer])
# Получаем итератор по объектам слоя
fts = layer.getFeatures()
# Получаем первый объект в итераторе
ft = fts.__next__()
# Выбираем данный объект
layer.selectByIds([ft.id()])
# Создаем буффер 
buff = ft.geometry().buffer(.2,8)
# Создаем слой для буффера
buffLyr =  QgsVectorLayer('Polygon?crs=epsg:4326', 'Buffer' , "memory")
# Получаем доступ к данный на слое
pr = buffLyr.dataProvider()
# Создаем новый объект
b = QgsFeature()
# Делаем геометрию объекта как у буффера
b.setGeometry(buff)
# Добавляем на слой
pr.addFeatures([b])
# Обновляем размеры слоя
buffLyr.updateExtents()
# Ставим прозрачность слоя
buffLyr.setOpacity(70/100)
# Добавляем слой в проект
QgsProject.instance().addMapLayers([buffLyr])
