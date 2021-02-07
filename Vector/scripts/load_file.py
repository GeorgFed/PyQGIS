layer = QgsVectorLayer("<NYC_MUSEUMS_GEO.shp FULL PATH>", "New York City Museums", "ogr")
if not layer.isValid():
  print("Layer {} did not load".format(layer.name()))
QgsProject.instance().addMapLayers([layer])
