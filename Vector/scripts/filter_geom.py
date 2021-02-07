# Слой с точками
lyrPts = QgsVectorLayer("D:/hse/GIS/qgis_vector/ms/MSCities_Geo_Pts.shp", "MSCities_Geo_Pts", "ogr")
# Слой с полигонами
lyrPoly = QgsVectorLayer("D:/hse/GIS/qgis_vector/ms/GIS_CensusTract_poly.shp", "GIS_CensusTract_poly", "ogr")
# Отображаем два слоя
QgsProject.instance().addMapLayers([lyrPoly,lyrPts])
# Получаем объекты слоя с полигонами
ftsPoly = lyrPoly.getFeatures()
# Проходимся по всем полигонам
for feat in ftsPoly:
    geomPoly = feat.geometry()
    bbox = geomPoly.boundingBox()
    req = QgsFeatureRequest()
    # Получаем массив точек, лежащих внутри рамок полигона
    filterRect = req.setFilterRect(bbox)
    featsPnt = lyrPts.getFeatures(filterRect)
    # Проверяем, какие из точек в рамках полигона лежат в самом полигоне
    for featPnt in featsPnt:
        # Лежащие точки выделяем
        if featPnt.geometry().within(geomPoly):
            print(featPnt.id())
            lyrPts.select(featPnt.id())
# Приближаем к полигону
iface.setActiveLayer(lyrPoly)
iface.zoomToActiveLayer() 
