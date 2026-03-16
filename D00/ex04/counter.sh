#!/bin/sh

tail -n +2 ../ex03/hh_positions.csv \
  | awk -F',' '{gsub(/"/,"",$3); if ($3 != "-") {print $3}}' \
  | sort \
  | uniq -c \
  | sort -nr \
  | awk 'BEGIN{OFS=","; print "\"name\",\"count\""} {gsub(/^ +/, "", $1); print "\"" $2 "\"," $1}' \
  > hh_uniq_positions.csv
