#!/bin/bash

cd $(dirname $0)
. $(dirname $0)/config.sh



cat arealabel.sql | psql $db
cat pitchicon.sql | psql $db
cat stationdirection.sql | psql $db
cat viewpointdirection.sql | psql $db

./update_isolations_from_topographic_isolation_viefinderpanoramas.txt.sh
./update_lowzoom_in_gis.sh
./update_parking.sh
