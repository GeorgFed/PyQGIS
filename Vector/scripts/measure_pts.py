lyr = QgsVectorLayer("D:/hse/GIS/project_qgis_repository/PyQGIS/Vector/scripts/nyc/NYC_MUSEUMS_GEO.shp", "Museums", "ogr")
fts = lyr.getFeatures()
first = fts.__next__()
last = fts.__next__()
for f in fts:
  last = f
d = QgsDistanceArea()
m = d.measureLine(first.geometry().asPoint(), last.geometry().asPoint())
print(d.convertLengthMeasurement(m, 0))