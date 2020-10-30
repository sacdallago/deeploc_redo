#!/bin/python

from pandas import read_csv

locations_mapping_file = "all_vs_all-automatically_mapped_swissprot_deeploc_localizations.csv"

locations_mapping = read_csv(locations_mapping_file, index_col=0)
locations_mapping = locations_mapping[['MANUAL_MAP']].dropna()

# Make sure you have 10 classes!
assert(len(locations_mapping['MANUAL_MAP'].unique()) == 10)

swissprot = read_csv("evidence_subcellular_localizations.csv")
swissprot_deeploc = swissprot.merge(locations_mapping, left_on="location", right_on="location", how="left").dropna()
swissprot_deeploc.to_csv("swissprot_with_deeploc_mapping.csv", index=False)
