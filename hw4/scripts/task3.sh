#!/bin/bash

cd .. && gawk -F',' ' BEGIN { OFS = "," } NR > 1 { if ($3 == 2 && substr($13, 1, 1) == "S") { print $0 } }' titanic.csv | sed 's/male/M/g; s/female/F/g' | gawk -F',' '$7 != "" {totalAges += $7; numAges++ } END { print totalAges/numAges; }'