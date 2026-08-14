from qgis import processing
from qgis.processing import alg

@alg(name='fix_geometries', label='04 - Fix Geometries', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Input vector layer')
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Fixed geometries output')
def fix_geometries(instance, parameters, context, feedback, inputs):
    """Repairs invalid vector geometries using QGIS native geometry fixing."""
    result = processing.run('native:fixgeometries', {'INPUT': parameters['INPUT'], 'METHOD': 1, 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
