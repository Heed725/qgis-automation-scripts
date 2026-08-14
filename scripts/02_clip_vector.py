from qgis import processing
from qgis.processing import alg

@alg(name='clip_vector', label='02 - Clip Vector Layer', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Input vector layer')
@alg.input(type=alg.SOURCE, name='OVERLAY', label='Clip polygon layer')
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Clipped output')
def clip_vector(instance, parameters, context, feedback, inputs):
    """Clips a vector layer using polygon features from another layer."""
    result = processing.run('native:clip', {'INPUT': parameters['INPUT'], 'OVERLAY': parameters['OVERLAY'], 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
