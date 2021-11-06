# -*- coding: utf-8 -*-

#structure de fichier 
from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       )
from qgis import processing


class ExampleProcessingAlgorithm(QgsProcessingAlgorithm):
   

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    
   
    
    def tr(self, string):   # Gérer les caractères
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

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
        # geometry.
        pass
        

        
    def processAlgorithm(self, parameters, context, feedback):
        pass
        
       
