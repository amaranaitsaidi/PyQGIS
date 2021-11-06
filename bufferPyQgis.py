from qgis.core import (QgsProcessingAlgorithm,
                       QgsProcessingParameterNumber,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFeatureSink)

import processing

class CreatBuffer(QgsProcessingAlgorithm):
    INPUT_BUFFERDIST = 'BUFFERDIST'
    OUTPUT_BUFFER = 'OUTPUT_BUFFER'
    INPUT_VECTOR = 'INPUT_VECTOR'

    def __init__(self):
        super().__init__()

    def name(self):
        return "algTest"

    def displayName(self):
        return "algTest script"

    def createInstance(self):
        return type(self)()

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterFeatureSource(
            self.INPUT_VECTOR, "Input vector"))
        self.addParameter(QgsProcessingParameterNumber(
            self.INPUT_BUFFERDIST, "Buffer distance",
            QgsProcessingParameterNumber.Double,
            10.0))
        self.addParameter(QgsProcessingParameterFeatureSink(
            self.OUTPUT_BUFFER, "Output buffer"))

    def processAlgorithm(self, parameters, context, feedback):

        bufferresult = processing.run('native:buffer',
                                      {'INPUT': parameters[self.INPUT_VECTOR],
                                       'DISTANCE': parameters[self.INPUT_BUFFERDIST],
                                       'SEGMENTS': 5,
                                       'END_CAP_STYLE': 0,
                                       'JOIN_STYLE': 0,
                                       'MITER_LIMIT': 10,
                                       'DISSOLVE': True,
                                       'OUTPUT': parameters[self.OUTPUT_BUFFER]},
                                      context=context, feedback=feedback, is_child_algorithm=True)
        buffered = bufferresult['OUTPUT']
        feedback.pushInfo('sink output number of features is')
        return {self.OUTPUT_BUFFER: buffered}