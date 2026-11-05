#!/bin/bash

variables=("pr" "tas")
periods=("historical" "scenario")

for var in "${variables[@]}"
do
    for period in "${periods[@]}"
    do

        if [ "$period" = "historical" ]; then
            echo "Processing historical data for $var"
        else
            echo "Processing scenario data for $var"
        fi
    done
done