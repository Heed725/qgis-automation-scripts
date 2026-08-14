from qgis import processing
from qgis.processing import alg

@alg(name='minimum_bounding_geometry', label='18 - Minimum Bounding Geometry', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Input vector layer')
@alg.input(type=alg.ENUM, name='TYPE', label='Geometry type', options=['Envelope','Minimum oriented rectangle','Minimum enclosing circle','Convex hull'], default=1)
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Bounding geometry output')
def minimum_bounding_geometry(instance, parameters, context, feedback, inputs):
    """Creates a chosen minimum bounding geometry around features."""
    result = processing.run('native:minimumboundinggeometry', {'INPUT': parameters['INPUT'], 'FIELD': None, 'TYPE': parameters['TYPE'], 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
