from qgis import processing
from qgis.processing import alg

@alg(name='difference_layers', label='10 - Difference', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Input layer')
@alg.input(type=alg.SOURCE, name='OVERLAY', label='Overlay layer')
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Difference output')
def difference_layers(instance, parameters, context, feedback, inputs):
    """Subtracts overlay geometries from the input vector layer."""
    result = processing.run('native:difference', {'INPUT': parameters['INPUT'], 'OVERLAY': parameters['OVERLAY'], 'GRID_SIZE': None, 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
