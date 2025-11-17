# VR Asset Optimizer

[![Blender](https://img.shields.io/badge/Blender-3.0%2B-orange.svg)](https://www.blender.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/Sudip13/AssetOptimizer)

> Complete VR asset optimization toolkit for Unity and Unreal Engine

Transform high-poly CAD models and 3D assets into optimized, game-ready VR assets with one click. Features automated mesh decimation, LOD generation, dual UV unwrapping, and intelligent vertex merging.

## ✨ Key Features

- 🎯 **One-Click Optimization** - Preset workflows for CAD imports, game assets, and VR
- 🔧 **Smart Decimation** - Reduce polys while maintaining quality with weighted normals
- 📦 **Auto LOD Generation** - Create 2-8 LOD levels with progressive decimation
- 🗺️ **Dual UV System** - UV0 for textures, UV1 for lightmaps
- ✨ **Vertex Cleanup** - Essential for CAD model imports
- 🎮 **Engine-Ready** - Unity and Unreal Engine export conventions

## 🚀 Quick Start

```python
# Install the addon in Blender 3.0+
1. Download and install ZIP
2. Open VR Assets panel (N key)
3. Select mesh objects
4. Click "CAD Import" or "Game Asset"
5. Export to Unity/Unreal
```

## 📊 Performance Impact

| Asset Type | Before | After | Improvement |
|------------|--------|-------|-------------|
| CAD Model | 250K polys | 60K polys | 76% reduction |
| Character | 150K polys | 45K polys | 70% reduction |
| Environment | 500K polys | 150K polys | 70% reduction |
| VR Scene | 2M polys | 400K polys | 80% reduction |

## 📖 Documentation

- [Installation Guide](INSTALL.md)
- [Usage Guide](USAGE_GUIDE.md)
- [Changelog](CHANGELOG.md)

## 🎯 Workflow Examples

### CAD to Unity
```
Import STEP → CAD Import Preset → Export FBX → Unity
Result: Clean, optimized mesh with dual UVs ready for lightmapping
```

### Game Asset Pipeline
```
High-Poly Model → Game Asset Preset → Export with LODs
Result: Optimized mesh with 3 LOD levels and dual UVs
```

### VR Optimization
```
Scene Objects → VR Optimized Preset → Export
Result: 70% poly reduction + 4 LOD levels + lightmap UVs
```

## 🛠️ Requirements

- Blender 3.0 or later
- Compatible with Blender 4.x
- Windows, macOS, or Linux

## 💡 Why Use This Addon?

**Manual Process (Traditional):**
- Merge vertices manually
- Apply modifiers one by one
- Create LODs by duplicating
- Unwrap UVs separately
- Rename objects for LODs
- Time: 30-60 minutes per asset

**With VR Asset Optimizer:**
- Select objects
- Click preset button
- Done!
- Time: 5-30 seconds per asset

## 📦 What's Included

- **5 Operators**: Batch optimize, decimate, LOD gen, dual UV, vertex merge
- **3 Presets**: CAD Import, Game Asset, VR Optimized
- **2 UV Layers**: UV0 (texturing) + UV1 (lightmaps)
- **8 LOD Levels**: Configurable progressive decimation
- **Multiple Algorithms**: Collapse, Un-Subdivide, Planar decimation

## 🎓 Learn More

Check out the [Usage Guide](USAGE_GUIDE.md) for:
- Step-by-step tutorials
- Workflow examples
- Pro tips
- Troubleshooting
- Best practices

## 🤝 Contributing

Contributions welcome! Please feel free to submit pull requests, report bugs, or suggest features.

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details

## 👤 Author

**Sudip Soni**
- GitHub: [@Sudip13](https://github.com/Sudip13)
- Repository: [AssetOptimizer](https://github.com/Sudip13/AssetOptimizer)

## ⭐ Support

If this addon helps your workflow, please star the repository!

---

**Made for VR developers by VR developers** 🥽
