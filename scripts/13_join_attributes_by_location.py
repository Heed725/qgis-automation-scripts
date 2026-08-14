from qgis import processing
from qgis.processing import alg

@alg(name='join_attributes_by_location', label='13 - Join Attributes By Location', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Base layer')
@alg.input(type=alg.SOURCE, name='JOIN', label='Join layer')
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Joined output')
def join_attributes_by_location(instance, parameters, context, feedback, inputs):
    """Joins attributes from spatially intersecting features."""
    result = processing.run('native:joinattributesbylocation', {'INPUT': parameters['INPUT'], 'JOIN': parameters['JOIN'], 'PREDICATE': [0], 'JOIN_FIELDS': [], 'METHOD': 0, 'DISCARD_NONMATCHING': False, 'PREFIX': '', 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
