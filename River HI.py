import rasterio
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
from rasterio.mask import mask

# DEM file
dem_file = r"C:\Users\91827\Downloads\Charles_uni\River_profile_data\DEM_data.tif"

# Basin shapefiles
basins = {
    "Alaknanda": r"C:\Users\91827\Downloads\Separate_basin\alakriver.shp",
    "Mandakini": r"C:\Users\91827\Downloads\Chaeles University assignment\shapefile\mandakinishape.shp",
    "Pindar": r"C:\Users\91827\Downloads\Chaeles University assignment\shapefile\Pindarshp.shp",
    "Dhauliganga": r"C:\Users\91827\Downloads\Separate_basin\dhaulipoly.shp",
    "Nandakini": r"C:\Users\91827\Downloads\Chaeles University assignment\shapefile\nandakinishp.shp"
}

# Store results
HI_results = {}

# Open DEM once
with rasterio.open(dem_file) as src:

    plt.figure(figsize=(8,6))

    for basin_name, basin_path in basins.items():

        basin = gpd.read_file(basin_path)

        dem_clip, transform = mask(
            src,
            basin.geometry,
            crop=True,
            filled=False
        )

        dem = dem_clip[0]
        nodata = src.nodata

        # Mask nodata
        dem = np.ma.masked_equal(dem, nodata)

        elev = dem.compressed()

        if len(elev) == 0:
            print(f"No valid DEM data for {basin_name}")
            continue

        
        # Elevation statistics
      
        z_min = np.min(elev)
        z_max = np.max(elev)

        relative_elev = (elev - z_min) / (z_max - z_min)

        relative_elev_sorted = np.sort(relative_elev)

        relative_area = np.arange(1, len(relative_elev_sorted)+1) / len(relative_elev_sorted)

        
        # Hypsometric Integral
       
        HI = (np.mean(elev) - z_min) / (z_max - z_min)

        HI_results[basin_name] = HI

       
        # Plot curve
       
        plt.plot(
            relative_area*100,
            relative_elev_sorted*100,
            linewidth=2,
            label=f"{basin_name} (HI={HI:.2f})"
        )


# Graph formatting

plt.xlabel("Relative Area (%)", fontsize=12.5)
plt.ylabel("Relative Elevation (%)", fontsize=12.5)

plt.title("Hypsometric Curve Comparison of Alaknanda Basin and Tributaries",
          fontsize=12.5)

plt.legend(fontsize=12.5)

plt.xticks(fontsize=12.5)
plt.yticks(fontsize=12.5)

plt.grid(True)

plt.tight_layout()

plt.savefig("Hypsometric_Comparison.png", dpi=600)

plt.show()


# Basin stage interpretation

print("\nHypsometric Integral Results:\n")

for basin, HI in HI_results.items():

    if HI > 0.6:
        stage = "Young Stage"
    elif HI > 0.35:
        stage = "Mature Stage"
    else:
        stage = "Old / Highly Eroded"

    print(f"{basin}: HI = {HI:.3f} → {stage}")