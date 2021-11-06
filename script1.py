# -*- coding: utf-8 -*-



from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterVectorLayer,
                       QgsProcessingParameterFeatureSink,
                       QgsProcessingParameterString)
from qgis import processing


class ExampleProcessingAlgorithm(QgsProcessingAlgorithm):
   

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    INPUT = 'INPUT'
    DISTANCE='DISTANCE'
    OUTPUT='OUTPUT'
   

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return ExampleProcessingAlgorithm()

    def name(self):
       
        return 'myscript'

    def displayName(self):
        
     
        return self.tr('My Script')

    def group(self):
       
        return self.tr('Example scripts')

    def groupId(self):
       
        return 'examplescripts'

    def shortHelpString(self):
       
        return self.tr("Example algorithm short description")

    def initAlgorithm(self, config=None):
       

        # We add the input vector features source. It can have any kind of
        # geometry.
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                self.INPUT,
                self.tr('Input layer')
            )
        )

        
    def processAlgorithm(self, parameters, context, feedback):
        
        couche = self.parameterAsVectorLayer(
            parameters,
            self.INPUT,
            context
        )
        
        feedback.pushInfo('sink output number of features is'+couche.name())
