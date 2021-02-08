# Создаем точки - последняя обзяательно должна быть равна первой для замыкания
p1 = QgsPointXY(1, 2)
p2 = QgsPointXY(2, 3)
p3 = QgsPointXY(-5, 2)
p4 = QgsPointXY(1, 2)
# Создаем слой
layer = QgsVectorLayer('Polygon', 'polygon' , 'memory')
prov = layer.dataProvider()
points = [p1,p2,p3,p4]
feat = QgsFeature()
# Добавляем на слой геометрию - полигон из нашего массива точек
feat.setGeometry(QgsGeometry.fromPolygonXY([points]))
# Добавляем объект
prov.addFeatures([feat])
layer.updateExtents()
# Отображаем
QgsProject.instance().addMapLayers([layer])