from qgis import processing
from qgis.processing import alg

@alg(name='intersection_layers', label='09 - Intersection', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Input layer')
@alg.input(type=alg.SOURCE, name='OVERLAY', label='Overlay layer')
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Intersection output')
def intersection_layers(instance, parameters, context, feedback, inputs):
    """Calculates the geometric intersection between two vector layers."""
    result = processing.run('native:intersection', {'INPUT': parameters['INPUT'], 'OVERLAY': parameters['OVERLAY'], 'INPUT_FIELDS': [], 'OVERLAY_FIELDS': [], 'OVERLAY_FIELDS_PREFIX': '', 'GRID_SIZE': None, 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
