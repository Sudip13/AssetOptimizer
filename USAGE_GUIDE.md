# Quick Start Guide

## 5-Minute Tutorial

### Scenario 1: Imported CAD Model

```
Goal: Clean up a STEP/IGES import and make it game-ready

Steps:
1. Import CAD file (File > Import > your format)
2. Select all imported objects (A key)
3. Open VR Assets panel (N key)
4. Click "CAD Import" button
5. Click OK in dialog

Result: Clean mesh, merged vertices, 60% poly reduction, dual UVs ready
```

### Scenario 2: Create Game Asset with LODs

```
Goal: Convert high-poly model to optimized game asset

Steps:
1. Select your high-poly model
2. Open VR Assets panel
3. Set Target Engine (Unity or Unreal)
4. Click "Game Asset" button
5. Review settings, click OK

Result: Optimized mesh with 3 LOD levels and dual UVs
```

### Scenario 3: VR Optimization

```
Goal: Aggressive optimization for VR performance

Steps:
1. Select scene objects
2. Open VR Assets panel
3. Click "VR Optimized" button
4. Confirm aggressive settings

Result: 70% poly reduction, 4 LOD levels, lightmap-ready
```

---

## Individual Tools Usage

### 1. Merge Vertices

**When to use:**
- Imported CAD models with duplicate vertices
- Meshes with overlapping geometry
- After boolean operations

**Steps:**
1. Select objects
2. Click "Merge Vertices"
3. Set merge distance (default: 0.0001)
4. Enable "Sharp Edges from Normals" to preserve hard edges
5. Click OK

**Tips:**
- Start with 0.0001 distance for precision models
- Use 0.001 for less precise cleanup
- Enable "Delete Loose" to remove stray vertices

---

### 2. Decimate Mesh

**When to use:**
- Reduce polygon count for performance
- Optimize high-poly sculpts
- Create base for LOD levels

**Steps:**
1. Select objects
2. Click "Decimate Mesh"
3. Choose decimation type:
   - **Collapse**: Best for organic models (default)
   - **Planar**: Best for architectural/CAD
   - **Un-Subdivide**: Remove subdivision levels
4. Set ratio (0.5 = 50% polys)
5. Enable weighted normals for smooth shading
6. Click OK

**Tips:**
- Use Collapse for characters/organic
- Use Planar for hard-surface/architecture
- Enable "Apply Modifiers" for final result
- Keep "Weighted Normals" ON for quality

---

### 3. Dual UV Unwrap

**When to use:**
- Need both texture and lightmap UVs
- Unity/Unreal lightmapping
- Multiple UV channels required

**Steps:**
1. Select objects
2. Click "Dual UV Unwrap (UV0 + UV1)"
3. Configure UV0 (texturing):
   - Method: Smart UV (recommended)
   - Enable packing
   - Small margin (0.001-0.02)
4. Configure UV1 (lightmaps):
   - Method: Lightmap Pack (recommended)
   - Larger margin (0.05)
5. Click OK

**Understanding UV Layers:**
- **UV0 (UVMap)**: For albedo/diffuse textures
  - Can have overlapping islands
  - Optimized for texture atlases
  - Supports rotation during packing
  
- **UV1 (UVMap_Lightmap)**: For baked lighting
  - Must NOT overlap
  - Larger margins prevent bleeding
  - Optimized for lightmap resolution

**Tips:**
- Always use Lightmap Pack for UV1
- Increase UV1 margin to 0.05+ for lightmaps
- UV0 can use any method depending on model
- Enable rotation for better UV0 packing

---

### 4. Generate LOD Groups

**When to use:**
- Creating game-ready assets
- VR optimization
- Performance-critical scenes

**Steps:**
1. Select base mesh (LOD0)
2. Click "Generate LOD Groups"
3. Choose target engine (Unity/Unreal)
4. Set LOD count (3-4 recommended)
5. Choose progression:
   - **Auto Progressive**: Automatic ratios (recommended)
   - **Manual**: Set each LOD ratio
6. Click OK

**LOD Level Guidelines:**
```
LOD0: 100%  - Full detail (0-10m distance)
LOD1: 50%   - Medium detail (10-25m distance)
LOD2: 25%   - Low detail (25-50m distance)
LOD3: 10%   - Very low (50-100m distance)
LOD4: 5%    - Minimal (100m+ distance)
```

**Tips:**
- Use 3 LODs for most assets
- Use 4+ LODs for hero/important objects
- VR needs aggressive LODs (more levels)
- Collections created automatically for organization

---

## Batch Optimization Presets

### CAD Import Preset
```
Enabled Steps:
✓ Merge Vertices (0.0001)
✓ Decimate (60% ratio)
✓ Dual UV Unwrap
✗ LOD Generation

Settings:
- Merge: Very precise (0.0001)
- Decimate: Conservative (60%)
- Sharp edge preservation: ON
- Weighted normals: ON
```

**Best for:**
- STEP files
- IGES files
- STL imports
- Solidworks exports

---

### Game Asset Preset
```
Enabled Steps:
✓ Merge Vertices (0.0001)
✓ Decimate (50% ratio)
✓ Dual UV Unwrap
✓ LOD Generation (3 levels)

Settings:
- Merge: Precise
- Decimate: Moderate (50%)
- LODs: 3 levels (progressive)
- Both UV layers generated
```

**Best for:**
- Props
- Environment assets
- Character models
- Standard game objects

---

### VR Optimized Preset
```
Enabled Steps:
✓ Merge Vertices (0.0001)
✓ Decimate (30% ratio)
✓ Dual UV Unwrap
✓ LOD Generation (4 levels)

Settings:
- Merge: Precise
- Decimate: Aggressive (30%)
- LODs: 4 levels (progressive)
- Lightmap UV prioritized
```

**Best for:**
- VR scenes
- Mobile VR
- Performance-critical assets
- Large-scale environments

---

## Workflow Examples

### Complete CAD to Unity Workflow

```
1. Import CAD Model
   File > Import > STEP/IGES

2. Initial Cleanup
   - Select all objects (A)
   - Object > Apply > All Transforms

3. Optimize with Addon
   - VR Assets panel > CAD Import preset
   - Confirm settings

4. Check Results
   - View poly count reduction in panel
   - Verify UV layers (2 layers)

5. Export to Unity
   - File > Export > FBX
   - Enable "Apply Transforms"
   - Enable "Apply Modifiers"

6. In Unity
   - Import FBX
   - Check UV0 in material
   - Enable lightmap UV (uses UV1)
   - Set to static for lightmapping
```

---

### Character Model to Unreal

```
1. Prepare Model
   - Select character mesh
   - Set Target Engine: Unreal

2. Optimize
   - Game Asset preset
   - OR Custom with settings:
     - Decimate: 40-50%
     - LODs: 3 levels
     - Dual UVs: ON

3. Check LODs
   - Verify LOD_0, LOD_1, LOD_2 created
   - Check poly counts in panel

4. Export
   - File > Export > FBX
   - Mesh > Smoothing: Face
   - Include LOD objects

5. In Unreal
   - Import FBX with LODs
   - LODs auto-detected
   - UV1 used for lightmaps
```

---

### VR Environment Optimization

```
1. Select All Scene Objects
   - A key (select all)
   - Or select specific objects

2. Set Target
   - Target Engine: Unity or Unreal
   - Choose based on project

3. Aggressive Optimize
   - VR Optimized preset
   - Review 70% reduction warning
   - Confirm

4. Review Results
   - Check poly count reduction
   - Verify 4 LOD levels per object
   - Check UV layers

5. Test Performance
   - Export to engine
   - Test on VR hardware
   - Adjust individual LODs if needed
```

---

## Pro Tips

### Performance Optimization
- Target 50K-100K total polys for VR scenes
- Use LODs on objects > 5K polys
- Prioritize objects in camera view
- Use occlusion culling in engine

### UV Mapping Best Practices
- UV0: Tiling textures OK, overlaps OK
- UV1: NO overlaps, NO tiling, proper margins
- Test lightmaps in engine before finalizing
- Increase UV1 margin if seeing light bleeding

### CAD Import Tips
- Always merge vertices first (CAD exports have duplicates)
- Use Planar decimation for architectural
- Check for inverted normals after import
- Scale appropriately before optimization

### LOD Strategy
- Set LOD distances in engine after export
- Hero objects: 4-5 LODs
- Background objects: 2-3 LODs
- Small props: 1-2 LODs
- Test LOD transitions in VR

---

## Troubleshooting

### Issue: Too much detail lost
**Solution:** Increase decimate ratio (higher = more detail)

### Issue: UVs overlapping in lightmap
**Solution:** Use Lightmap Pack for UV1, increase margin to 0.1

### Issue: Shading looks faceted
**Solution:** Enable weighted normals and auto smooth

### Issue: LODs not working in Unity
**Solution:** Check naming (ObjectName_LOD0), reimport FBX

### Issue: Vertices not merging
**Solution:** Increase merge distance slightly (try 0.001)

---

## Keyboard Shortcuts

- `N` - Toggle sidebar (show/hide panel)
- `A` - Select all objects
- `Alt+A` - Deselect all
- `Tab` - Toggle Edit/Object mode
- `Z` - View shading menu

---

## Next Steps

1. ✓ Learn the basics (you're here!)
2. ⭐ Try each preset on sample models
3. 🎯 Practice individual tools
4. 🚀 Export to your engine
5. 📊 Profile performance gains
6. 🎨 Apply to production assets

---

**Questions?** [Open an Issue](https://github.com/Sudip13/AssetOptimizer/issues) or check the main [README](README.md)
