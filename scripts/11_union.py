from qgis import processing
from qgis.processing import alg

@alg(name='union_layers', label='11 - Union', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Input layer')
@alg.input(type=alg.SOURCE, name='OVERLAY', label='Overlay layer')
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Union output')
def union_layers(instance, parameters, context, feedback, inputs):
    """Creates the geometric union of two vector layers."""
    result = processing.run('native:union', {'INPUT': parameters['INPUT'], 'OVERLAY': parameters['OVERLAY'], 'OVERLAY_FIELDS_PREFIX': '', 'GRID_SIZE': None, 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
