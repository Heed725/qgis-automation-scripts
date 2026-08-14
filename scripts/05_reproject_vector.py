from qgis import processing
from qgis.processing import alg

@alg(name='reproject_vector', label='05 - Reproject Vector Layer', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Input vector layer')
@alg.input(type=alg.CRS, name='TARGET_CRS', label='Target CRS', default='EPSG:4326')
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Reprojected output')
def reproject_vector(instance, parameters, context, feedback, inputs):
    """Reprojects a vector layer to a selected coordinate reference system."""
    result = processing.run('native:reprojectlayer', {'INPUT': parameters['INPUT'], 'TARGET_CRS': parameters['TARGET_CRS'], 'OPERATION': '', 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
