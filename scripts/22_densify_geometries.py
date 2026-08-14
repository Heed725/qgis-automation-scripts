from qgis import processing
from qgis.processing import alg

@alg(name='densify_geometries', label='22 - Densify Geometries', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Input vector layer')
@alg.input(type=alg.DISTANCE, name='INTERVAL', label='Maximum vertex interval', default=100.0)
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Densified output')
def densify_geometries(instance, parameters, context, feedback, inputs):
    """Adds vertices so geometry segments do not exceed the selected interval."""
    result = processing.run('native:densifygeometriesgivenaninterval', {'INPUT': parameters['INPUT'], 'INTERVAL': parameters['INTERVAL'], 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
