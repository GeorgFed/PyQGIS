lyrPts = QgsVectorLayer("D:/hse/GIS/project_qgis_repository/PyQGIS/Vector/scripts/nyc/NYC_MUSEUMS_GEO.shp", "Museums", "ogr")
QgsProject.instance().addMapLayers([lyrPts])
# Фильтруем объекты по ZIP-коду 
selection = lyrPts.getFeatures(QgsFeatureRequest().setFilterExpression(u'"ZIP" = 10002'))
# Выделяем отфильторванные точки
lyrPts.selectByIds([s.id() for s in selection])
# Приближаем выделенные точки
iface.mapCanvas().zoomToSelected()
