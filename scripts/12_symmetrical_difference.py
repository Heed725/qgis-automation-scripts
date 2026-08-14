from qgis import processing
from qgis.processing import alg

@alg(name='symmetrical_difference', label='12 - Symmetrical Difference', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Input layer')
@alg.input(type=alg.SOURCE, name='OVERLAY', label='Overlay layer')
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Symmetrical difference output')
def symmetrical_difference(instance, parameters, context, feedback, inputs):
    """Returns areas belonging to either input layer but not to both."""
    result = processing.run('native:symmetricaldifference', {'INPUT': parameters['INPUT'], 'OVERLAY': parameters['OVERLAY'], 'OVERLAY_FIELDS_PREFIX': '', 'GRID_SIZE': None, 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
