from qgis import processing
from qgis.processing import alg

@alg(name='polygon_to_lines', label='14 - Polygons To Lines', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Polygon layer')
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Line output')
def polygon_to_lines(instance, parameters, context, feedback, inputs):
    """Converts polygon boundaries to line features."""
    result = processing.run('native:polygonstolines', {'INPUT': parameters['INPUT'], 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
