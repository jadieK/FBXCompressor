from fbx import *

def modify_animation(scene):
    for anim_stack_index in range(scene.GetSrcObjectCount(FbxCriteria.ObjectType(FbxAnimStack.ClassId))):
        anim_stack = scene.GetSrcObject(FbxCriteria.ObjectType(FbxAnimStack.ClassId), anim_stack_index)
        print('<Animation Modifier> : Processing animation stack - ' + anim_stack.GetName())
        _modify_animation_stack(anim_stack, scene.GetRootNode())


def _modify_animation_stack(animation_stack, node):
    for anim_layer_index in range(animation_stack.GetSrcObjectCount(FbxCriteria.ObjectType(FbxAnimLayer.ClassId))):
        anim_layer = animation_stack.GetSrcObject(FbxCriteria.ObjectType(FbxAnimLayer.ClassId), anim_layer_index)
        print('<Animation Modifier> : Processing animation layer - ' + anim_layer.GetName())
        _modify_animation_layer(anim_layer, node)


def _modify_animation_layer(animation_layer, node):
    print('<Animation Modifier> : Processing Node - ' + node.GetName())
    _modify_channels(animation_layer, node)
    for node_index in range(node.GetChildCount()):
        _modify_animation_layer(animation_layer, node.GetChild(node_index))


target_channels = ['X', 'Y', 'Z']
target_properties = ['LclTranslation', 'LclRotation', 'LclScaling']


def _modify_channels(animation_layer, node):
    for current_property in target_properties:
        for current_channel in target_channels:
            command = 'node.' + current_property + '.GetCurve(animation_layer, "' + current_channel + '")'
            result = eval(command)
            if result:
                result.KeyModifyBegin()
                for key_index in range(result.KeyGetCount()):
                    old_value = result.KeyGetValue(key_index)
                    new_value = float('%.3f' % old_value)
                    print('<Animation Modifier> : Processing Channels Before is ' + str(old_value) + ' After is ' + str(new_value))
                    result.KeySetValue(key_index, new_value)
                result.KeyModifyEnd()

