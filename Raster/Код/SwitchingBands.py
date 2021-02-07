rasterLyr = QgsRasterLayer("/Users/georg/Downloads/SatImage/SatImage.tif", "Band Swap")
if rasterLyr.isValid():
    ren = rasterLyr.renderer()
    ren.setGreenBand(1)
    QgsProject.instance().addMapLayers([rasterLyr])
    