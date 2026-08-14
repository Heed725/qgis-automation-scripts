from qgis import processing
from qgis.processing import alg

@alg(name='buffer_features', label='01 - Buffer Features', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.SOURCE, name='INPUT', label='Input vector layer')
@alg.input(type=alg.DISTANCE, name='DISTANCE', label='Buffer distance', default=100.0)
@alg.input(type=alg.NUMBER, name='SEGMENTS', label='Segments', default=5)
@alg.input(type=alg.BOOL, name='DISSOLVE', label='Dissolve result', default=False)
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Buffered output')
def buffer_features(instance, parameters, context, feedback, inputs):
    """Buffers vector features with configurable distance, segments, and dissolve option."""
    result = processing.run('native:buffer', {'INPUT': parameters['INPUT'], 'DISTANCE': parameters['DISTANCE'], 'SEGMENTS': int(parameters['SEGMENTS']), 'END_CAP_STYLE': 0, 'JOIN_STYLE': 0, 'MITER_LIMIT': 2, 'DISSOLVE': parameters['DISSOLVE'], 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
