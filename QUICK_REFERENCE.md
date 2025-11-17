# Quick Reference Card

## 🎯 VR Asset Optimizer - Quick Reference

---

## Installation
```
Edit > Preferences > Add-ons > Install > Select ZIP > Enable
```

## Access Panel
```
Press N key > VR Assets tab
```

---

## 🚀 Quick Presets

| Preset | Use Case | Settings |
|--------|----------|----------|
| **CAD Import** | Imported CAD models | Merge + Decimate 60% + Dual UV |
| **Game Asset** | Standard game objects | Merge + Decimate 50% + Dual UV + 3 LODs |
| **VR Optimized** | VR performance | Merge + Decimate 30% + Dual UV + 4 LODs |
| **Custom** | Manual control | Configure all settings |

---

## 🔧 Individual Tools

### Merge Vertices
```
Use: CAD imports, cleanup
Default: 0.0001 distance
Tip: Enable sharp edge preservation
```

### Decimate Mesh
```
Use: Reduce poly count
Types: Collapse (organic) | Planar (CAD) | Un-Subdivide
Ratio: 0.5 = 50% polys
Tip: Keep weighted normals ON
```

### Dual UV Unwrap
```
UV0: Texturing (Smart UV)
UV1: Lightmaps (Lightmap Pack)
Margin: 0.02 (UV0) | 0.05 (UV1)
Tip: UV1 must not overlap
```

### Generate LODs
```
Levels: 3-4 recommended
Naming: Unity (Object_LOD0) | Unreal (Object_LOD_0)
Tip: Use progressive mode
```

---

## 📊 LOD Guidelines

| LOD | Ratio | Distance | Use |
|-----|-------|----------|-----|
| LOD0 | 100% | 0-10m | Full detail |
| LOD1 | 50% | 10-25m | Medium |
| LOD2 | 25% | 25-50m | Low |
| LOD3 | 10% | 50-100m | Very low |

---

## 🎨 UV Layers

| Layer | Name | Purpose | Overlap | Margin |
|-------|------|---------|---------|--------|
| UV0 | UVMap | Texturing | ✅ OK | 0.001-0.02 |
| UV1 | UVMap_Lightmap | Lightmaps | ❌ NO | 0.05+ |

---

## 🎮 Export Settings

### Unity
```
Format: FBX
Apply Transforms: ✓
Apply Modifiers: ✓
LOD Format: ObjectName_LOD0
```

### Unreal
```
Format: FBX
Mesh > Smoothing: Face
Generate Lightmap UVs: ✗ (already have UV1)
LOD Format: ObjectName_LOD_0
```

---

## ⚡ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `N` | Toggle sidebar |
| `A` | Select all |
| `Alt+A` | Deselect all |
| `Tab` | Edit/Object mode |

---

## 🐛 Quick Fixes

**Problem** → **Solution**

Too much detail lost → Increase decimate ratio  
UVs overlapping → Use Lightmap Pack for UV1  
Shading looks bad → Enable weighted normals  
LODs not working → Check naming format  
Vertices not merging → Increase merge distance  

---

## 📈 Typical Results

- **Vertex Merge**: 10-30% reduction
- **Decimation**: 40-90% reduction
- **LOD System**: 50-95% draw call reduction
- **Processing Time**: 5-30 seconds per asset

---

## 💡 Pro Tips

1. Always merge vertices first for CAD
2. Use Lightmap Pack for UV1
3. Test LOD distances in engine
4. Start conservative, iterate
5. Check results before exporting

---

## 🔗 Quick Links

- Full Docs: `README.md`
- Tutorials: `USAGE_GUIDE.md`
- Install: `INSTALL.md`
- Updates: `CHANGELOG.md`

---

**Print this card for quick reference!** 📄
