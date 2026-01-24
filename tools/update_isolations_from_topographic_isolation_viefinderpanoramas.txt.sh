#Alternatively, if the isolations calculation is too long, you can download the computed dominance from :
# https://geo.dianacht.de/topo/topographic_isolation_viefinderpanoramas.txt

. $(dirname $0)/config.sh

echo "creating the otm_isolation column to hold isolation information of peaks..."
psqld -d $db -c "ALTER TABLE planet_osm_point ADD COLUMN otm_isolation text;" 

echo "creating an index on osm_id because osm2pgsql newer versions does no create it anymore, and we need it to update peak isolation..."
psql -d $db -c "create index IF NOT EXISTS planet_osm_point_osm_id on planet_osm_point (osm_id);"
echo "done"

echo "Updating isolation on all peaks and Volcanos..."
wget -q https://geo.dianacht.de/topo/topographic_isolation_viefinderpanoramas.txt -O - | egrep -v '^#' | sed s/"\([0-9]*;\).*;.*;\([0-9]*\)"/"update planet_osm_point set otm_isolation=\2 where osm_id=\1"/g | psql -q $db
echo "done"


