#!/bin/sh

header=$(head -n 1 $(ls *.csv | grep -v 'hh_positions_concat.csv' | head -n1))
echo "$header" > hh_positions_concat.csv

for f in *.csv; do
  [ "$f" = "hh_positions_concat.csv" ] && continue
  tail -n +2 "$f" >> hh_positions_concat.csv
done
