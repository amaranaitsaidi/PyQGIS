from qgis.utils import iface
from qgis.core import QgsSymbol,QgsRendererCategory,QgsCategorizedSymbolRenderer
from PyQt5.QtGui import QColor


layer = iface.activeLayer()
# define a lookup: value -> (color, label) dictionnaire avec les catégorie et ses couleurs et une étiquette
category = {
    'PBO': ('#f00', 'PBO'), #couleur rouge et étiquette PBO
    'BPI': ('#0f0', 'BPI'), #couleur verte et étiquette PBO
    'PIQUAGE': ('#fff', 'PIQUAGE'),
    '': ('#000', 'DEFAULT'), #quant il trouve rien il met par défaut noir et l'étiquette default
}

# create a category for each item in animals
categories = []
for cat, (color, label) in category.items():
    symbol = QgsSymbol.defaultSymbol(layer.geometryType()) #récupérer la géométrie de la couche
    symbol.setColor(QColor(color)) # appliquer la couleur du dictionnaire en fonction du filtre de la couche
    #symbol.setSize(10)
    category = QgsRendererCategory(cat, symbol, label) # choisir de catégorisé les couleur (équivalement sympbologie dans qgis) cat pour catégorisé
    categories.append(category) #compléter la liste categorie 

# create the renderer and assign it to a layer
expression = 'type_fonc' # field name l'élément sur lequel on applique le filtre 
renderer = QgsCategorizedSymbolRenderer(expression, categories) # on applique les categorie sur les expressions
layer.setRenderer(renderer)


iface.mapCanvas().refresh()  