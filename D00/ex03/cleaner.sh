#!/bin/sh
awk -F',' 'BEGIN{OFS=","}
NR==1 {print; next}
{
  pos=$3
  gsub(/^"|"$/,"",pos)
  if (pos ~ /Junior/ && pos ~ /Middle/ && pos ~ /Senior/) {pos="Junior/Middle/Senior"}
  else if (pos ~ /Junior/ && pos ~ /Middle/) {pos="Junior/Middle"}
  else if (pos ~ /Junior/ && pos ~ /Senior/) {pos="Junior/Senior"}
  else if (pos ~ /Middle/ && pos ~ /Senior/) {pos="Middle/Senior"}
  else if (pos ~ /Junior/) {pos="Junior"}
  else if (pos ~ /Middle/) {pos="Middle"}
  else if (pos ~ /Senior/) {pos="Senior"}
  else {pos="-"}
  $3="\"" pos "\""
  print
}' ../ex02/hh_sorted.csv > hh_positions.csv


