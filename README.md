# OpenHikingMap-new
OpenHikingMap-new is a mapnik 3+ map style using Openstreetmap data focused on Hiking. This style uses OpenTopoMap : https://github.com/sletuffe/OpenTopoMap as a base, extended with several POI mainly used in hiking/trail activities.

As of 2026-01-24 it is still under developpement and there is no demo, it aims at replacing https://wiki.openstreetmap.org/wiki/OpenHikingMap

Missing external files can be found :

== geotiff files for relief, contours pg dump and Water Areas shapefiles ==

This still uses pre-compiled or data not from OpenStreetMap
You can get the one I'm using here : https://openmaps.fr/download

But of course you can build your own colored or not & shaded or not relief

== water polygons ==

Source & more accurate polygons are here :
https://osmdata.openstreetmap.de/data/water-polygons.html


== DEM Data ==
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

