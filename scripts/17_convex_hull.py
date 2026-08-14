from qgis import processing
from qgis.processing import alg

@alg(name='convex_hull', label='17 - Convex Hull', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Input vector layer')
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Convex hull output')
def convex_hull(instance, parameters, context, feedback, inputs):
    """Creates convex hull polygons around input features."""
    result = processing.run('native:convexhull', {'INPUT': parameters['INPUT'], 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
