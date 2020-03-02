from fbx import *
from os import linesep


def display_hierarchy(scene):
    root_node = scene.GetRootNode()
    for current_child_index in range(root_node.GetChildCount()):
        _display_hierarchy(root_node.GetChild(current_child_index), 0)


def _display_hierarchy(target_node, depth):
    prefix = '-'
    for current_depth in range(depth):
        prefix += '-'

    print(prefix + target_node.GetName())

    for child_index in range(target_node.GetChildCount()):
        _display_hierarchy(target_node.GetChild(child_index), depth + 1)
