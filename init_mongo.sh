#!/usr/bin/env bash

export MONGO_INITDB_DATABASE=intelygenz

mongoimport --host localhost --db $MONGO_INITDB_DATABASE --collection restaurant --type json --file /restaurant.json
