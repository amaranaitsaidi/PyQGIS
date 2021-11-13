# -*- coding: utf-8 -*-


from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSink,
                       QgsProcessingParameterVectorLayer,
                       QgsProcessingParameterExpression,
                       QgsVectorLayer
                       )
from qgis import processing


class ExampleProcessingAlgorithm(QgsProcessingAlgorithm):
   

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    INPUT='INPUT'
    EXP='EXP'
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
        
     
        return self.tr('select_by_exp')

    def group(self):
       
        return self.tr('select_by_exp')

    def groupId(self):
       
        return 'select_by_exp'

    def shortHelpString(self):
       
        return self.tr("Example algorithm short description")

    def initAlgorithm(self, config=None):
        
        self.addParameter(QgsProcessingParameterVectorLayer(
                self.INPUT,
                self.tr('Input layer')
            )
        )
        
        self.addParameter(
            QgsProcessingParameterExpression(
                self.EXP,
                self.tr('Expression'),
                parentLayerParameterName=self.INPUT
            )
        )
        
        self.addParameter(QgsProcessingParameterFeatureSink(
            self.OUTPUT, "Output"))

        
       

        # configurer les parametres
        # geometry.
        
        

        
    def processAlgorithm(self, parameters, context, feedback):
        
        couche = self.parameterAsVectorLayer(
            parameters,
            self.INPUT,
            context
        )
        expression=self.parameterAsExpression(
            parameters,
            self.EXP,
            context
        )
        
        couche.selectByExpression(expression,
        QgsVectorLayer.SetSelection)
        
        communes_select=processing.run('qgis:saveselectedfeatures',
        {'INPUT':couche,
        'OUTPUT':parameters[self.OUTPUT]},
        context=context, feedback=feedback, is_child_algorithm=True)
        mescommunes=communes_select['OUTPUT']
        
        
        
        return {self.OUTPUT: mescommunes}
        
        
       
