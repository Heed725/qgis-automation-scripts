from qgis import processing
from qgis.processing import alg

@alg(name='extract_vertices', label='16 - Extract Vertices', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Input vector layer')
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Vertices output')
def extract_vertices(instance, parameters, context, feedback, inputs):
    """Creates point features for every vertex in the input geometries."""
    result = processing.run('native:extractvertices', {'INPUT': parameters['INPUT'], 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
