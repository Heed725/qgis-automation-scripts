from qgis import processing
from qgis.processing import alg

@alg(name='dissolve_features', label='03 - Dissolve Features', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Input vector layer')
@alg.input(type=alg.FIELD, name='FIELD', label='Dissolve field', parentLayerParameterName='INPUT', optional=True, allowMultiple=True)
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Dissolved output')
def dissolve_features(instance, parameters, context, feedback, inputs):
    """Dissolves all features or groups them by one or more selected fields."""
    fields = parameters.get('FIELD') or []
    result = processing.run('native:dissolve', {'INPUT': parameters['INPUT'], 'FIELD': fields, 'SEPARATE_DISJOINT': False, 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
