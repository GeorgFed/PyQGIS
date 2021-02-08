vectorLyr =  QgsVectorLayer('/Users/georg/Downloads/PyQGIS-main/Vector/scripts/nyc/NYC_MUSEUMS_GEO.shp', 'Museums' , "ogr")
vpr = vectorLyr.dataProvider()
# Берем ID объекта, который будем двигать
feat_id = 22
geom = QgsGeometry.fromPointXY(QgsPointXY(-74.20378,40.89642))
# Меняем значение расположения объекта с заданным ID
vpr.changeGeometryValues({feat_id : geom })