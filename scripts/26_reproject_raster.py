from qgis import processing
from qgis.processing import alg

@alg(name='reproject_raster', label='26 - Reproject Raster', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.RASTER_LAYER, name='INPUT', label='Input raster')
@alg.input(type=alg.CRS, name='TARGET_CRS', label='Target CRS', default='EPSG:4326')
@alg.input(type=alg.ENUM, name='RESAMPLING', label='Resampling', options=['Nearest neighbour','Bilinear','Cubic','Cubic spline','Lanczos'], default=0)
@alg.input(type=alg.RASTER_LAYER_DEST, name='OUTPUT', label='Reprojected raster output')
def reproject_raster(instance, parameters, context, feedback, inputs):
    """Reprojects a raster to a chosen CRS using a selected resampling method."""
    result = processing.run('gdal:warpreproject', {'INPUT': parameters['INPUT'], 'SOURCE_CRS': None, 'TARGET_CRS': parameters['TARGET_CRS'], 'RESAMPLING': parameters['RESAMPLING'], 'NODATA': None, 'TARGET_RESOLUTION': None, 'OPTIONS': '', 'DATA_TYPE': 0, 'TARGET_EXTENT': None, 'TARGET_EXTENT_CRS': None, 'MULTITHREADING': False, 'EXTRA': '', 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
