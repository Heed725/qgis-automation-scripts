# QGIS Automation Scripts

A collection of 30 reusable QGIS Processing scripts written in Python/PyQGIS. The scripts are designed to appear in the **Processing Toolbox > Scripts > QGIS Automation Scripts** group and cover common vector, raster, terrain, geometry-cleaning, overlay, conversion, and data-preparation workflows.

## Included scripts

1. Buffer Features
2. Clip Vector Layer
3. Dissolve Features
4. Fix Geometries
5. Reproject Vector Layer
6. Extract By Expression
7. Create Centroids
8. Multipart To Singleparts
9. Intersection
10. Difference
11. Union
12. Symmetrical Difference
13. Join Attributes By Location
14. Polygons To Lines
15. Lines To Polygons
16. Extract Vertices
17. Convex Hull
18. Minimum Bounding Geometry
19. Delete Holes
20. Simplify Geometries
21. Smooth Geometries
22. Densify Geometries
23. Merge Vector Layers
24. Random Points In Extent
25. Clip Raster By Mask
26. Reproject Raster
27. DEM Hillshade
28. DEM Slope
29. DEM Aspect
30. Raster Polygonize

## Installation

### Option 1: Copy scripts into the QGIS Processing scripts folder

1. Download or clone this repository.
2. Open QGIS.
3. Open **Processing > Toolbox**.
4. In the Processing Toolbox, expand **Scripts**.
5. Choose **Open Scripts Folder** from the Scripts menu.
6. Copy all `.py` files from this repository's `scripts/` directory into that folder.
7. Refresh the Processing Toolbox or restart QGIS.
8. The algorithms will appear under **Scripts > QGIS Automation Scripts**.

### Option 2: Open and save individual scripts

Use **Processing Toolbox > Scripts > Create New Script**, paste the contents of a script, and save it in the default scripts directory.

## Requirements

- QGIS 3.x with the Processing framework enabled.
- GDAL Processing provider enabled for the raster clipping, raster reprojection, and polygonize scripts.

The scripts use QGIS Processing's `@alg` decorator, native QGIS algorithms, and GDAL algorithms. They are intended for modern QGIS 3.x releases.

## Repository structure

```text
qgis-automation-scripts/
├── README.md
└── scripts/
    ├── 01_buffer_features.py
    ├── 02_clip_vector.py
    ├── ...
    └── 30_raster_polygonize.py
```

## Usage

Open any algorithm from the Processing Toolbox, choose its inputs and output destination, and run it like any built-in QGIS Processing algorithm. Because these are Processing algorithms, they can also be used in the Graphical Modeler, batch processing, and other Processing workflows.

## Notes

- Distances use the units of the relevant layer/CRS unless QGIS indicates otherwise.
- For meaningful distance/area operations, use a suitable projected CRS.
- Validate source data before large overlay jobs; the included **Fix Geometries** script can help with invalid geometries.
- Some GDAL parameter names can differ between major QGIS/GDAL generations; the scripts target the QGIS 3.x Processing API.

## License

You may add your preferred open-source license to this repository.
