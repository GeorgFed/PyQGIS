vectorLyr =  QgsVectorLayer('/Users/georg/Downloads/PyQGIS-main/Vector/scripts/nyc/NYC_MUSEUMS_GEO.shp', 'Museums' , "ogr")
vpr = vectorLyr.dataProvider()
# Берем ID объекта, свойства которого будем менять
feat_id1 = 22
feat_id2 = 23
tel = vectorLyr.fields().indexFromName('TEL')
city = vectorLyr.fields().indexFromName('CITY')
attr1 = {tel:'(123)111-11-11', city: 'NYC'}
attr2 = {tel:'(123)111-22-22', city: 'NYC'}
# Меняем значение расположения объекта с заданным ID
vpr.changeAttributeValues({feat_id: attr1, feat_id2: attr2})