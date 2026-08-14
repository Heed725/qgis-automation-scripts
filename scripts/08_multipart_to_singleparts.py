from qgis import processing
from qgis.processing import alg

@alg(name='multipart_to_singleparts', label='08 - Multipart To Singleparts', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Input vector layer')
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Singlepart output')
def multipart_to_singleparts(instance, parameters, context, feedback, inputs):
    """Splits multipart geometries into individual singlepart features."""
    result = processing.run('native:multiparttosingleparts', {'INPUT': parameters['INPUT'], 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
