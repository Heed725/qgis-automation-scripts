from qgis import processing
from qgis.processing import alg

@alg(name='create_centroids', label='07 - Create Centroids', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Input vector layer')
@alg.input(type=alg.BOOL, name='ALL_PARTS', label='Create centroid for each part', default=False)
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Centroids output')
def create_centroids(instance, parameters, context, feedback, inputs):
    """Creates centroid points for input geometries."""
    result = processing.run('native:centroids', {'INPUT': parameters['INPUT'], 'ALL_PARTS': parameters['ALL_PARTS'], 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
