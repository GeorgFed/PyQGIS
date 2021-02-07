lyrPts = QgsVectorLayer("D:/hse/GIS/qgis_vector/ms/MSCities_Geo_Pts.shp", "MSCities_Geo_Pts", "ogr")
lyrPoly = QgsVectorLayer("D:/hse/GIS/qgis_vector/ms/GIS_CensusTract_poly.shp", "GIS_CensusTract_poly", "ogr")
QgsProject.instance().addMapLayers([lyrPoly,lyrPts])
ftsPoly = lyrPoly.getFeatures()
for feat in ftsPoly:
    geomPoly = feat.geometry()
    bbox = geomPoly.boundingBox()
    req = QgsFeatureRequest()
    filterRect = req.setFilterRect(bbox)
    featsPnt = lyrPts.getFeatures(filterRect)
    for featPnt in featsPnt:
        if featPnt.geometry().within(geomPoly):
            print(featPnt.id())
            lyrPts.select(featPnt.id())

iface.setActiveLayer(lyrPoly)
iface.zoomToActiveLayer() 