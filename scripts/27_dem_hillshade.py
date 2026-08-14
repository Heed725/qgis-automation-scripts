from qgis import processing
from qgis.processing import alg

@alg(name='dem_hillshade', label='27 - DEM Hillshade', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.RASTER_LAYER, name='INPUT', label='DEM raster')
@alg.input(type=alg.NUMBER, name='Z_FACTOR', label='Z factor', default=1.0)
@alg.input(type=alg.NUMBER, name='AZIMUTH', label='Azimuth', default=300.0)
@alg.input(type=alg.NUMBER, name='V_ANGLE', label='Vertical angle', default=40.0)
@alg.input(type=alg.RASTER_LAYER_DEST, name='OUTPUT', label='Hillshade output')
def dem_hillshade(instance, parameters, context, feedback, inputs):
    """Creates a hillshade raster from a digital elevation model."""
    result = processing.run('native:hillshade', {'INPUT': parameters['INPUT'], 'Z_FACTOR': parameters['Z_FACTOR'], 'AZIMUTH': parameters['AZIMUTH'], 'V_ANGLE': parameters['V_ANGLE'], 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
