#!/bin/sh

header=$(head -n 1 ../ex03/hh_positions.csv)

tail -n +2 ../ex03/hh_positions.csv | while IFS= read -r line; do
    d=$(echo "$line" | cut -d',' -f2 | cut -c2-11)
    if [ ! -f "$d.csv" ]; then
        echo "$header" > "$d.csv"
    fi
    echo "$line" >> "$d.csv"
done
