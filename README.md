# Hypsometric Analysis & Basin Geomorphology using DEM and Geospatial Python

## Overview

This repository contains a Python-based geomorphometric workflow for generating hypsometric curves and calculating Hypsometric Integral (HI) from Digital Elevation Models (DEMs) and watershed boundary datasets.

The workflow evaluates basin-scale terrain evolution, erosion status, and geomorphic maturity through relative elevation–area analysis and comparative basin morphometry.

This project is designed for applications in:

- Fluvial geomorphology
- Basin morphometry
- Watershed analysis
- Terrain evolution studies
- Hydrology
- Environmental geomatics
- Mountain landscape analysis

---

## Features

- Clip DEM using watershed boundaries
- Generate hypsometric curves automatically
- Calculate Hypsometric Integral (HI)
- Compare multiple basins simultaneously
- Classify geomorphic development stages
- Produce publication-quality visualizations
- Basin-scale terrain evolution analysis

---

## Technologies Used

- Python
- Rasterio
- GeoPandas
- NumPy
- Matplotlib

---

## Workflow

1. Load DEM raster
2. Load watershed shapefiles
3. Clip DEM for each basin
4. Extract elevation values
5. Normalize elevation and basin area
6. Generate hypsometric curves
7. Compute Hypsometric Integral (HI)
8. Interpret geomorphic maturity stages
9. Visualize comparative basin evolution

---

## Input Data

### Required Inputs

#### 1. DEM Raster
- Digital Elevation Model
- Format: `.tif`

#### 2. Basin Boundary Shapefiles
- Watershed polygon shapefiles
- Format: `.shp`

---

## Example Outputs

The workflow generates:

- Comparative hypsometric curves
- Hypsometric Integral (HI) values
- Basin evolution stage interpretation
- High-resolution geomorphic visualizations

---

## Geomorphic Interpretation

Hypsometric Integral values are used to classify watershed evolutionary stages:

| HI Value | Basin Stage |
|---|---|
| > 0.60 | Young Stage |
| 0.35 – 0.60 | Mature Stage |
| < 0.35 | Old / Highly Eroded Stage |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/hypsometric-analysis-basin-geomorphology.git
cd hypsometric-analysis-basin-geomorphology
```

Install required packages:

```bash
pip install rasterio geopandas numpy matplotlib
```

---

## Usage

Update the DEM and basin shapefile paths:

```python
dem_file = r"path_to_dem.tif"

basins = {
    "Basin_Name": r"path_to_basin.shp"
}
```

Run the script:

```bash
python hypsometric_analysis.py
```

---

## Methodology

### Relative Elevation

Elevation is normalized using:

```math
h/H = \frac{z - z_{min}}{z_{max} - z_{min}}
```

### Relative Area

Relative basin area is computed as cumulative area percentage.

### Hypsometric Integral

Hypsometric Integral is calculated using:

```math
HI = \frac{\bar{z} - z_{min}}{z_{max} - z_{min}}
```

where:

- \( \bar{z} \) = mean elevation
- \( z_{min} \) = minimum elevation
- \( z_{max} \) = maximum elevation

---

## Applications

- Basin evolution studies
- Watershed geomorphology
- Tectonic geomorphology
- Landscape maturity assessment
- Mountain basin analysis
- River basin comparison
- Erosion and denudation studies

---

## Future Improvements

- Automated watershed extraction
- Stream order integration
- Relief ratio computation
- Drainage density analysis
- Interactive GIS visualization
- Multi-temporal terrain evolution analysis

---

## Repository Structure

```bash
hypsometric-analysis-basin-geomorphology/
│
├── data/
│   ├── dem/
│   └── basin_shapefiles/
│
├── outputs/
│   ├── figures/
│   └── statistics/
│
├── hypsometric_analysis.py
├── requirements.txt
└── README.md
```

---

## Author

Akash A  
M.Tech Remote Sensing Student  
Indian Institute of Technology Roorkee

---

## License

This project is released under the MIT License.

---

## Citation

If you use this workflow in research or academic work, please cite this repository appropriately.

```bibtex
@software{hypsometric_analysis_basin_geomorphology,
  author = {Akash A},
  title = {Hypsometric Analysis and Basin Geomorphology using DEM and Geospatial Python},
  year = {2026},
  url = {https://github.com/yourusername/hypsometric-analysis-basin-geomorphology}
}
```
