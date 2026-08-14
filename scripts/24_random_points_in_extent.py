from qgis import processing
from qgis.processing import alg

@alg(name='random_points_in_extent', label='24 - Random Points In Extent', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.EXTENT, name='EXTENT', label='Target extent')
@alg.input(type=alg.NUMBER, name='POINTS_NUMBER', label='Number of points', default=100)
@alg.input(type=alg.DISTANCE, name='MIN_DISTANCE', label='Minimum distance', default=0.0)
@alg.input(type=alg.CRS, name='TARGET_CRS', label='CRS', default='EPSG:4326')
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Random points output')
def random_points_in_extent(instance, parameters, context, feedback, inputs):
    """Generates random points within a chosen map extent."""
    result = processing.run('native:randompointsinextent', {'EXTENT': parameters['EXTENT'], 'POINTS_NUMBER': int(parameters['POINTS_NUMBER']), 'MIN_DISTANCE': parameters['MIN_DISTANCE'], 'TARGET_CRS': parameters['TARGET_CRS'], 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
