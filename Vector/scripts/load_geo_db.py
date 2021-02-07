# Созадем экземпляр базы данных
uri = QgsDataSourceURI()
# Устанавливаем связь с базой данных
uri.setConnection("spacialdb.com", "9999", "lzmjzm_hwpqlf", "lzmjzm_hwpqlf", "0e9fcc39")
# Описываем источник данных
uri.setDataSource("public", "islands", "wkb_geometry", "")
# Создаем слой
layer = QgsVectorLayer(uri.uri(), "Islands", "postgres")
# Проверяем корректность слоя
if not layer.isValid():
  print "Layer %s did not load" % layer.name()
# Добавляем слой на карту
QgsMapLayerRegistry.instance().addMapLayers([layer]) 
