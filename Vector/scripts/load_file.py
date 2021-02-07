layer = QgsVectorLayer("D:/hse/GIS/qgis_vector/nyc/NYC_MUSEUMS_GEO.shp", "New York City Museums", "ogr")
if not layer.isValid():
  print("Layer {} did not load".format(layer.name()))
QgsProject.instance().addMapLayers([layer])