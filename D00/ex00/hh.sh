#!/bin/bash
vacancy="$1"
curl -s "https://api.hh.ru/vacancies?text=${vacancy// /%}&per_page=20"  | jq '.' > hh.json