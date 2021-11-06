# -*- coding: utf-8 -*-

#structure de fichier 
from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterString,
                       QgsProcessingParameterVectorLayer,
                       QgsProcessingParameterField,
                       QgsProcessingParameterExpression,
                       )
from qgis import processing

class ExampleProcessingAlgorithm(QgsProcessingAlgorithm):
   

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.
    
    # on définit nos variables avant les fonctions 
    texte= "texte"
    couche_input = "couche_input"
    colonne ="colonne"
    exp = "exp"
    
    def tr(self, string):
        
        return QCoreApplication.translate("Processing", string)
        
       
    def createInstance(self): # instance de notre algorithme
        return ExampleProcessingAlgorithm()

    def name(self): # le nom qui va s'afficher dans la liste des scripts
       
        return 'scriptg2m'

    def displayName(self): # Le nom qui s'affiche dans la fenêtre 
             
        return self.tr('My Script')

    def group(self): # le nom du groupe ou on regroupe les scripts du même pour le même projet
       
        return self.tr('Goupe G2M')

    def groupId(self): 
       
        return 'examplescripts'

    def shortHelpString(self): #description de l'outil  
       
        return self.tr("Example algorithm short description")
        
        
    # ces deux fonction sont les plus importantes 
    
    def initAlgorithm(self, config=None): # définir les paramètres  
            

        # configurer les parametres
        #self.addParameter est à utiliser à chaque fois qu'on veut ajouter un paramètre
        self.addParameter(QgsProcessingParameterString(
            self.texte, #récupérer la variable définit plus haut 
            self.tr('Saisir un text')
        ))
        
        # geometry.
        self.addParameter(QgsProcessingParameterVectorLayer(
            self.couche_input, #récupérer la variable définit plus haut 
            self.tr('Selectionner une couche')
        ))
        
        self.addParameter(QgsProcessingParameterField(
            self.colonne, #récupérer la variable définit plus haut 
            self.tr('Colonne choisie'),
            parentLayerParameterName = "couche_input"
        ))
        self.addParameter(QgsProcessingParameterExpression(
            self.exp, #récupérer la variable définit plus haut 
            self.tr('exppression'),
            parentLayerParameterName = "couche_input" # on laisse le paramètre pour récupérer dans champs de valeur
        ))
      

        
    def processAlgorithm(self, parameters, context, feedback):   # récupérer la valeur saisie par l'utilisateur
      
        saisie_utilisateur = self.parameterAsString(
            parameters, # nomenclature par défaut de qgis  
            self.texte, # on récupère la valeur du text
            context
            )
       
        couche_choisie = self.parameterAsVectorLayer(
            parameters, # nomenclature par défaut de qgis  
            self.couche_input, # on récupère la valeur du text
            context
            )
        expression = self.parameterAsExpression(
            parameters, # nomenclature par défaut de qgis  
            self.exp, # on récupère la valeur du text
            context
            )
        print(expression)
       
