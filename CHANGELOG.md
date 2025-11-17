# Changelog

All notable changes to VR Asset Optimizer will be documented in this file.

## [2.0.0] - 2024-11-17

### Added
- 🎯 **Batch Optimization System**
  - CAD Import preset for imported models
  - Game Asset preset for standard optimization
  - VR Optimized preset for aggressive optimization
  - Custom preset for manual control

- 🔧 **Automated Mesh Decimation**
  - Multiple decimation algorithms (Collapse, Un-Subdivide, Planar)
  - Weighted normal modifier support
  - Auto-smooth with customizable angles
  - Optional triangulation for game engines

- 📦 **LOD Generation System**
  - Generate 2-8 LOD levels automatically
  - Progressive decimation with auto-calculation
  - Unity and Unreal Engine naming conventions
  - Automatic collection organization
  - Per-LOD weighted normals

- 🗺️ **Dual UV Unwrapping**
  - UV0 layer for texturing (multiple methods)
  - UV1 layer for lightmapping
  - Smart UV projection
  - Lightmap Pack algorithm
  - Cube, Cylinder, Sphere projections
  - Island packing with rotation
  - Multi-object support

- ✨ **Smart Vertex Merging**
  - Merge vertices by distance
  - Sharp edge preservation
  - Degenerate geometry removal
  - Loose vertex cleanup
  - Automatic normal recalculation

- 🎨 **Comprehensive UI**
  - Selection statistics (poly count, vertex count)
  - Target engine selection (Unity/Unreal)
  - Individual tool access
  - UV layer information display
  - Advanced settings panel
  - Tips and recommendations

- 📚 **Documentation**
  - Complete README with all features
  - Installation guide
  - Usage guide with examples
  - Workflow tutorials
  - Troubleshooting section

### Changed
- Complete rewrite from scratch with modular architecture
- Improved operator organization
- Enhanced error handling and reporting
- Better multi-object processing

### Technical
- Blender 3.0+ compatibility
- Blender 4.x support
- Modular operator system
- Centralized properties management
- Helper utilities for common tasks

---

## [1.4.0] - Legacy

### Features
- Basic multi-object UV unwrap
- Smart UV projection
- Island packing
- Preset system (High Quality, Fast, Tight Pack, No Pack)

---

## Future Roadmap

### Planned for 2.1.0
- [ ] Material optimization tools
- [ ] Texture atlas generation
- [ ] Batch export functionality
- [ ] Animation LOD support
- [ ] Custom LOD distance settings

### Planned for 2.2.0
- [ ] Normal map baking
- [ ] Ambient occlusion baking
- [ ] Collision mesh generation
- [ ] NavMesh optimization
- [ ] Blueprint support for Unreal

### Community Requests
- [ ] Godot Engine support
- [ ] glTF export presets
- [ ] Automated retopology
- [ ] PBR material setup
- [ ] Real-time preview

---

## Contributing

Want to contribute? Check out our [Contributing Guidelines](CONTRIBUTING.md) (coming soon)

## Support

- Report bugs: [Issues](https://github.com/Sudip13/AssetOptimizer/issues)
- Feature requests: [Discussions](https://github.com/Sudip13/AssetOptimizer/discussions)
