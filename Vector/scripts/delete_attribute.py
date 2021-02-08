vectorLyr =  QgsVectorLayer('/Users/georg/Downloads/PyQGIS-main/Vector/scripts/nyc/NYC_MUSEUMS_GEO.shp', 'Museums' , "ogr")
vpr = vectorLyr.dataProvider()
# Берем ID объекта, который будем удалять
feat_id = 22
vpr.deleteAttributes([1])
vectorLyr.updateFields()
