# Создаем в памяти векторный слой, передаем ему свойства через &
vectorLyr =  QgsVectorLayer('Point?crs=epsg:4326&field=city:string(25)&field=population=int', 'Layer 1' , "memory")
print(vectorLyr.isValid())
# Вывод: True