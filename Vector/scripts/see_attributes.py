layer = QgsVectorLayer("D:/hse/GIS/qgis_vector/nyc/NYC_MUSEUMS_GEO.shp", "New York City Museums", "ogr")
features = layer.getFeatures()
f = feature.__next__()
f.attributes()