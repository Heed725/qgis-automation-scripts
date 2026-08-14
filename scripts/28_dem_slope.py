from qgis import processing
from qgis.processing import alg

@alg(name='dem_slope', label='28 - DEM Slope', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.RASTER_LAYER, name='INPUT', label='DEM raster')
@alg.input(type=alg.NUMBER, name='Z_FACTOR', label='Z factor', default=1.0)
@alg.input(type=alg.RASTER_LAYER_DEST, name='OUTPUT', label='Slope output')
def dem_slope(instance, parameters, context, feedback, inputs):
    """Calculates terrain slope from a digital elevation model."""
    result = processing.run('native:slope', {'INPUT': parameters['INPUT'], 'Z_FACTOR': parameters['Z_FACTOR'], 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
