# le module processing est essentiel pour utiliser les fonctions de QGIS
import processing

                #Import de la couche communes

layer_path = r"D:\Cours\PYTONHQGIS\Data\communes_idf.shp"
vlayer = iface.addVectorLayer(layer_path, "communesLayer", "ogr")
layer = iface.activeLayer()
# if not vlayer:
   #print("Layer failed to load!")
 
                #liste des processing
#for alg in QgsApplication.processingRegistry().algorithms():
    #print(alg.id(), "->", alg.displayName())
    
#pour utiliser une fonction on fait processing. + le nom de la fonction 
processing.algorithmHelp("gdal:buffervectors") # avoir l'aide sur l'utilisation de la fonction.


processing.run("gdal:buffervectors",
{'INPUT' : layer,
'DISTANCE' : 0.1,
'OUTPUT': "D:\\Cours\\PYTONHQGIS\\Data\\buffer.shp"})


