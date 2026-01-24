OpenTopoMap
===========
OpenTopoMap is a topographic mapnik 3+ xml (non CartoCss) map style using data from OpenStreetMap contributors and various Data Elevation Model. Created by @der-stefan, @max-dn and others.

As of 2026-01-20 3 world wide accessible instances exists that I know of : 
* The "main one" is at https://opentopomap.org ("OpenTopoMap backup") limited to zoom 15
* A fork in a docker container ( https://github.com/krusty82/otm-meins ) with viewer at https://top-o-map.de/
* One using this repo whose README you are reading right now, [visible at openmaps.fr](https://openmaps.fr/#opentopomap-r/5/46.34693/9.27246)

This instance of OpenTopoMap can also be used in other applications.
If you include tiles from tile.openmaps.fr in your project, you must read and accept the [Tile usage policy](https://openmaps.fr/tile-usage-policy.html) where you will also find the URLs for this map style.

Map's legend...
===============
Can be seen here [OTM-R's map legend](https://openmaps.fr/otm/legend.html)

OpenTopoMap-Revived
===================
This instance, that I'd like to call OTM-R (for OpenTopoMap-Revived or OpenTopoMap-Raster) for the time beeing, aims to be identical to the main instance's map for now and act as a failover/clone/in place replacement. While hoping to get help or time someday to improve the map itself. 
Except for a few changes :
* Contours, hillshading and elevation color was composed and kindly provided by @Yvecai from https://www.opensnowmap.org and based on :
  * ASTER GDEM is a product of METI and NASA
  * SRTM 1 Arc-Second Global
  * EU-DEM: Prroduced using Copernicus data and information funded by the European Union
  * France – RGE ALTI® 5m © IGN
  * Switzerland – Alti3D © swisstopo
  * US & Canada – NED 1arcsec U.S. Geological Survey
  * Austria – DHM 10m - CC-BY-4.0: Land Kärnten - data.gv.at
  * Italy – Tinitaly 10m – CC BY 4.0 Tarquini S., I. Isola, M. Favalli, A. Battistini, G. Dotta (2023). Istituto Nazionale di Geofisica e Vulcanologia (INGV).
  * Norway - DTM 10 Terrengmodell (UTM33) – CC BY 4.0 Kartverket

* Geotiff files (One for color+shade and one for shade) were merged into two tiff with overviews to reduce the xml code and number of files
* the "contours" table in it's own database was move to the gis database
* the lowzooms tables were put back into the gis database
* saddle icons orientation was postponed (all are shown vertical : ][)
* Contours are not shown over lakes or sea, and 0m lines were re-added

