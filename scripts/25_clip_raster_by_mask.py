from qgis import processing
from qgis.processing import alg

@alg(name='clip_raster_by_mask', label='25 - Clip Raster By Mask', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.RASTER_LAYER, name='INPUT', label='Input raster')
@alg.input(type=alg.SOURCE, name='MASK', label='Mask polygon layer')
@alg.input(type=alg.RASTER_LAYER_DEST, name='OUTPUT', label='Clipped raster output')
def clip_raster_by_mask(instance, parameters, context, feedback, inputs):
    """Clips a raster to the exact boundary of a polygon mask layer."""
    result = processing.run('gdal:cliprasterbymasklayer', {'INPUT': parameters['INPUT'], 'MASK': parameters['MASK'], 'SOURCE_CRS': None, 'TARGET_CRS': None, 'TARGET_EXTENT': None, 'NODATA': None, 'ALPHA_BAND': False, 'CROP_TO_CUTLINE': True, 'KEEP_RESOLUTION': False, 'SET_RESOLUTION': False, 'X_RESOLUTION': None, 'Y_RESOLUTION': None, 'MULTITHREADING': False, 'OPTIONS': '', 'DATA_TYPE': 0, 'EXTRA': '', 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
