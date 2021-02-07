# Используя путь к векторном файлу NYC_MUSEUMS_GEO.shp создаем слой
layer = QgsVectorLayer("<NYC_MUSEUMS_GEO.shp FULL PATH>", "New York City Museums", "ogr")
# Проверяем корректность создания слоя
if not layer.isValid():
  # Выводим ошибку создания слоя
  print("Layer {} did not load".format(layer.name()))
# Добавляем векторный слой на карту
QgsProject.instance().addMapLayers([layer])
