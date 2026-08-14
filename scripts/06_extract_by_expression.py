from qgis import processing
from qgis.processing import alg

@alg(name='extract_by_expression', label='06 - Extract By Expression', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Input vector layer')
@alg.input(type=alg.EXPRESSION, name='EXPRESSION', label='QGIS expression', parentLayerParameterName='INPUT', default='1 = 1')
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Matching features output')
def extract_by_expression(instance, parameters, context, feedback, inputs):
    """Extracts features matching any valid QGIS expression."""
    result = processing.run('native:extractbyexpression', {'INPUT': parameters['INPUT'], 'EXPRESSION': parameters['EXPRESSION'], 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
