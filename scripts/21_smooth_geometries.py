from qgis import processing
from qgis.processing import alg

@alg(name='smooth_geometries', label='21 - Smooth Geometries', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Input vector layer')
@alg.input(type=alg.NUMBER, name='ITERATIONS', label='Iterations', default=1)
@alg.input(type=alg.NUMBER, name='OFFSET', label='Offset (0-0.5)', default=0.25)
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Smoothed output')
def smooth_geometries(instance, parameters, context, feedback, inputs):
    """Smooths lines or polygons using configurable iterations and offset."""
    result = processing.run('native:smoothgeometry', {'INPUT': parameters['INPUT'], 'ITERATIONS': int(parameters['ITERATIONS']), 'OFFSET': parameters['OFFSET'], 'MAX_ANGLE': 180, 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
