from qgis import processing
from qgis.processing import alg

@alg(name='simplify_geometries', label='20 - Simplify Geometries', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Input vector layer')
@alg.input(type=alg.DISTANCE, name='TOLERANCE', label='Tolerance', default=1.0)
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Simplified output')
def simplify_geometries(instance, parameters, context, feedback, inputs):
    """Simplifies vector geometries using a distance tolerance."""
    result = processing.run('native:simplifygeometries', {'INPUT': parameters['INPUT'], 'METHOD': 0, 'TOLERANCE': parameters['TOLERANCE'], 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
