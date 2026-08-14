from qgis import processing
from qgis.processing import alg

@alg(name='lines_to_polygons', label='15 - Lines To Polygons', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Line layer')
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Polygon output')
def lines_to_polygons(instance, parameters, context, feedback, inputs):
    """Converts closed linework into polygon features."""
    result = processing.run('native:linestopolygons', {'INPUT': parameters['INPUT'], 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
