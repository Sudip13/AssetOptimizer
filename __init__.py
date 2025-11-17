bl_info = {
    "name": "VR Asset Optimizer",
    "author": "Sudip Soni",
    "version": (1, 0, 1),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > VR Assets",
    "description": "Complete VR asset optimization toolkit - mesh decimation, LOD generation, dual UV unwrap, and CAD model optimization for Unity and Unreal Engine",
    "warning": "",
    "doc_url": "https://github.com/Sudip13/AssetOptimizer",
    "tracker_url": "https://github.com/Sudip13/AssetOptimizer/issues",
    "support": "COMMUNITY",
    "category": "3D View",
}

import bpy
from . import operators
from . import ui
from . import utils


def register():
    """Register all addon classes and properties"""
    utils.register()
    operators.register()
    ui.register()


def unregister():
    """Unregister all addon classes and properties"""
    ui.unregister()
    operators.unregister()
    utils.unregister()


if __name__ == "__main__":
    register()
