from qgis import processing
from qgis.processing import alg

@alg(name='raster_polygonize', label='30 - Raster Polygonize', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.RASTER_LAYER, name='INPUT', label='Input raster')
@alg.input(type=alg.NUMBER, name='BAND', label='Band number', default=1)
@alg.input(type=alg.STRING, name='FIELD', label='Output value field name', default='DN')
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Polygon output')
def raster_polygonize(instance, parameters, context, feedback, inputs):
    """Converts raster regions with the same pixel value into vector polygons."""
    result = processing.run('gdal:polygonize', {'INPUT': parameters['INPUT'], 'BAND': int(parameters['BAND']), 'FIELD': parameters['FIELD'], 'EIGHT_CONNECTEDNESS': False, 'EXTRA': '', 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
