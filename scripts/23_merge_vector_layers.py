from qgis import processing
from qgis.processing import alg

@alg(name='merge_vector_layers', label='23 - Merge Vector Layers', group='qgisautomation', group_label='QGIS Automation Scripts')
@alg.input(type=alg.MULTILAYER, name='LAYERS', label='Vector layers to merge')
@alg.input(type=alg.CRS, name='CRS', label='Output CRS', optional=True)
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Merged output')
def merge_vector_layers(instance, parameters, context, feedback, inputs):
    """Merges multiple vector layers into a single output layer."""
    result = processing.run('native:mergevectorlayers', {'LAYERS': parameters['LAYERS'], 'CRS': parameters.get('CRS'), 'OUTPUT': parameters['OUTPUT']}, context=context, feedback=feedback)
    return {'OUTPUT': result['OUTPUT']}
