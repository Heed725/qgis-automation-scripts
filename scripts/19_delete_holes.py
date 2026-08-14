from qgis import processing
from qgis.processing import alg

@alg(name='delete_holes', label='19 - Delete Holes', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Polygon layer')
@alg.input(type=alg.NUMBER, name='MIN_AREA', label='Delete holes smaller than area (0 = all)', default=0.0)
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Output without holes')
def delete_holes(instance, parameters, context, feedback, inputs):
    """Removes polygon holes, optionally using a minimum area threshold."""
    result = processing.run('native:deleteholes', {'INPUT': parameters['INPUT'], 'MIN_AREA': parameters['MIN_AREA'], 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
