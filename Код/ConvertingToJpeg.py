from osgeo import gdal
# Создаем драйвер с нужным форматом
drv = gdal.GetDriverByName("JP2OpenJPEG")
# Открываем изначальное изображение
src = gdal.Open("/Users/georg/Downloads/SatImage/SatImage.tif")
# Копируем изображение с новым форматом
tgt = drv.CreateCopy('/Users/georg/Downloads/SatImage/SatImage2.jp2', src)