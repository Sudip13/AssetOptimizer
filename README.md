# VR Asset Optimizer - Blender Addon

**Developer**: [Sudip Soni](https://github.com/Sudip13)  
**Version**: 2.0.0  
**Repository**: [https://github.com/Sudip13/AssetOptimizer](https://github.com/Sudip13/AssetOptimizer)

A comprehensive Blender addon for optimizing 3D assets for VR applications in Unity and Unreal Engine. This toolkit combines mesh decimation, LOD generation, dual UV unwrapping, and CAD model cleanup into a streamlined workflow.

---

## Features

### 🎯 **One-Click Batch Optimization**
- **CAD Import Preset**: Optimize imported CAD models with vertex merging, decimation, and dual UV unwrap
- **Game Asset Preset**: Convert models to game-ready assets with LOD generation
- **VR Optimized Preset**: Aggressive optimization for VR performance
- **Custom Preset**: Full control over all optimization parameters

### 🔧 **Automated Mesh Decimation**
- Multiple decimation algorithms (Collapse, Un-Subdivide, Planar)
- Weighted normal modifier for smooth shading
- Auto-smooth with customizable angles
- Preserves visual quality while reducing poly count
- Optional triangulation for game engines

### 📦 **LOD Generation System**
- Generate 2-8 LOD levels automatically
- Progressive decimation with customizable ratios
- Unity and Unreal Engine naming conventions
- Automatic collection organization
- Smart weighted normals per LOD level

### 🗺️ **Dual UV Unwrapping**
- **UV0**: Optimized for texturing (Smart UV, Lightmap Pack, Cube, Cylinder, Sphere projections)
- **UV1**: Dedicated lightmap UV with proper margins
- Multiple unwrapping methods per UV layer
- Island packing with rotation optimization
- Multi-object support with separate UV spaces

### ✨ **Smart Vertex Merging**
- Merge vertices by distance (essential for CAD models)
- Sharp edge preservation based on normal angles
- Degenerate geometry removal
- Loose vertex/edge cleanup
- Automatic normal recalculation

---

## Installation

### Method 1: Download and Install
1. Download this repository as a ZIP file
2. Open Blender (3.0 or later)
3. Go to `Edit > Preferences > Add-ons`
4. Click `Install...` and select the downloaded ZIP file
5. Enable "VR Asset Optimizer" by checking the box

### Method 2: Manual Installation
1. Download/clone this repository
2. Copy the entire `AssetOptimizer` folder to your Blender addons directory:
   - **Windows**: `%APPDATA%\Blender Foundation\Blender\[version]\scripts\addons\`
   - **macOS**: `~/Library/Application Support/Blender/[version]/scripts/addons/`
   - **Linux**: `~/.config/blender/[version]/scripts/addons/`
3. Restart Blender
4. Enable the addon in `Preferences > Add-ons`

---

## Usage

### Quick Start - Batch Optimization

1. **Select** your mesh objects in the 3D viewport
2. Open the **VR Assets** panel in the sidebar (`N` key)
3. Choose your workflow:
   - **CAD Import**: For imported CAD models (STEP, IGES, etc.)
   - **Game Asset**: For standard game objects
   - **VR Optimized**: For aggressive VR optimization
   - **Custom**: For manual control

4. Set your **Target Engine** (Unity or Unreal)
5. Click the optimization preset button
6. Review and confirm settings in the dialog

### Individual Tools

#### 🔹 Merge Vertices
Perfect for CAD models that have duplicate vertices:
- Select objects
- Click "Merge Vertices"
- Adjust merge distance (default: 0.0001)
- Enable sharp edge preservation

#### 🔹 Decimate Mesh
Reduce polygon count while maintaining quality:
- Select objects
- Click "Decimate Mesh"
- Choose decimation type (Collapse, Un-Subdivide, or Planar)
- Set target ratio (0.5 = 50% of original polys)
- Enable weighted normals and auto smooth

#### 🔹 Dual UV Unwrap
Generate both texture and lightmap UVs:
- Select objects
- Click "Dual UV Unwrap (UV0 + UV1)"
- Configure UV0 for texturing (Smart UV recommended)
- Configure UV1 for lightmaps (Lightmap Pack recommended)
- Adjust margins and packing options

#### 🔹 Generate LOD Groups
Create LOD hierarchy for VR optimization:
- Select objects
- Click "Generate LOD Groups"
- Set number of LOD levels (2-8)
- Choose target engine (Unity/Unreal)
- Use auto-progressive ratios or manual control

---

## Workflow Examples

### CAD Model Import Workflow
```
1. Import CAD model (File > Import > CAD formats)
2. Select imported objects
3. VR Assets panel > "CAD Import" preset
4. Result: Clean mesh with proper UVs, ready for texturing
```

### Game Asset Creation Workflow
```
1. Create or import high-poly model
2. Select model
3. VR Assets panel > "Game Asset" preset
4. Result: Optimized model with LODs and dual UVs
```

### VR Optimization Workflow
```
1. Select existing scene objects
2. VR Assets panel > "VR Optimized" preset
3. Result: Heavily optimized meshes with 4 LOD levels
```

---

## Technical Details

### File Structure
```
AssetOptimizer/
├── __init__.py                    # Main addon entry
├── operators/
│   ├── __init__.py
│   ├── mesh_decimation.py        # Decimation operator
│   ├── lod_generator.py          # LOD generation
│   ├── dual_uv_unwrap.py         # Dual UV system
│   ├── vertex_merge.py           # Vertex merging
│   └── batch_optimizer.py        # Batch processing
├── ui/
│   ├── __init__.py
│   └── main_panel.py             # Main UI panel
├── utils/
│   ├── __init__.py
│   ├── properties.py             # Addon properties
│   └── helpers.py                # Helper functions
└── README.md
```

### Compatibility
- **Blender Version**: 3.0+ (4.x compatible)
- **Mode Requirements**: Works in Object mode
- **Object Types**: Mesh objects only

### UV Layer Naming
- **UV0**: `UVMap` (texturing)
- **UV1**: `UVMap_Lightmap` (lightmapping)

### LOD Naming Conventions
- **Unity**: `ObjectName_LOD0`, `ObjectName_LOD1`, etc.
- **Unreal**: `ObjectName_LOD_0`, `ObjectName_LOD_1`, etc.

---

## Export Guidelines

### Unity Export
1. Select optimized objects
2. `File > Export > FBX (.fbx)`
3. Settings:
   - Apply Transforms: ✓
   - Apply Modifiers: ✓
   - Object Types: Mesh
4. Import in Unity and assign to LOD Group component

### Unreal Engine Export
1. Select optimized objects
2. `File > Export > FBX (.fbx)`
3. Settings:
   - Apply Transforms: ✓
   - Apply Modifiers: ✓
   - Mesh > Smoothing: Face
4. Import in Unreal with "Generate Lightmap UVs" disabled (already have UV1)

---

## Presets Explained

### CAD Import Preset
- ✓ Merge Vertices (0.0001 distance)
- ✓ Decimate (60% ratio)
- ✓ Dual UV Unwrap
- ✗ LOD Generation

**Best for**: STEP, IGES, STL imports

### Game Asset Preset
- ✓ Merge Vertices (0.0001 distance)
- ✓ Decimate (50% ratio)
- ✓ Dual UV Unwrap
- ✓ LOD Generation (3 levels)

**Best for**: Standard game objects

### VR Optimized Preset
- ✓ Merge Vertices (0.0001 distance)
- ✓ Decimate (30% ratio - aggressive)
- ✓ Dual UV Unwrap
- ✓ LOD Generation (4 levels)

**Best for**: VR applications where performance is critical

---

## Tips & Best Practices

### For CAD Models
- Always merge vertices first (CAD exports often have duplicate vertices)
- Use planar decimation for architectural models
- Start with conservative merge distance (0.0001)

### For VR Optimization
- Target 10K-50K polygons for LOD0
- Generate at least 3 LOD levels
- Use lightmap UVs (UV1) for baked lighting
- Test on target VR hardware

### For UV Unwrapping
- UV0 (texturing): Can have overlapping islands for tiling
- UV1 (lightmaps): MUST NOT have overlapping islands
- Use larger margins for lightmap UVs (0.05+)
- Pack islands to maximize texture space

### For LOD Generation
- LOD0: Full detail (100%)
- LOD1: Medium detail (50-60%)
- LOD2: Low detail (20-30%)
- LOD3+: Very low detail (5-10%)

---

## Troubleshooting

### "No mesh objects selected"
**Solution**: Make sure you have mesh objects selected in Object mode

### UV unwrap fails
**Solution**: Ensure objects have faces (not just vertices/edges)

### Decimation removes too much detail
**Solution**: Increase the ratio or use weighted normals for better quality

### LODs not appearing in Unity
**Solution**: Check naming convention matches Unity's LOD system (ObjectName_LOD0)

### Lightmaps look wrong in-engine
**Solution**: Ensure UV1 has no overlapping islands and sufficient margin

---

## Performance Metrics

### Typical Results
- **Vertex Merge**: 10-30% vertex reduction on CAD models
- **Decimation**: 40-90% polygon reduction (depending on settings)
- **LOD System**: 50-95% draw call reduction in VR
- **UV Generation**: < 1 second per object for dual UVs

---

## Changelog

### Version 2.0.0
- ✨ Complete rewrite with modular architecture
- ✨ Added batch optimization presets
- ✨ Enhanced dual UV system with multiple unwrap methods
- ✨ LOD generation with Unity/Unreal naming conventions
- ✨ Smart vertex merging with edge preservation
- ✨ Comprehensive UI with selection info and tips
- ✨ Advanced settings panel
- ✨ Multi-object processing for all operations

### Version 1.4.0 (Legacy)
- Basic multi-object UV unwrap
- Smart UV projection
- Island packing

---

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

### How to Contribute:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

This addon is provided as-is for educational and commercial use. Feel free to modify and distribute according to your needs.

---

## Support

- 🐛 **Issues**: [Report Bugs](https://github.com/Sudip13/AssetOptimizer/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Sudip13/AssetOptimizer/discussions)
- 📧 **Contact**: [Sudip Soni](https://github.com/Sudip13)

---

## Acknowledgments

- Blender Foundation for the amazing open-source 3D software
- Unity and Unreal Engine communities for VR optimization best practices
- CAD community for feedback on import workflows

---

**Made with ❤️ by [Sudip Soni](https://github.com/Sudip13) for the VR development community**
