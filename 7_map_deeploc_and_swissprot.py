#!/bin/python

from pandas import read_csv

deeploc = read_csv("filtered_deeploc_annotations.csv")
swissprot = read_csv("evidence_subcellular_localizations.csv")

deeploc_unique = deeploc[['accession', 'annotation']].drop_duplicates()
swissprot_unique = swissprot[['accession', 'location']].drop_duplicates()

merged = swissprot_unique.merge(deeploc_unique, how="left", on="accession")
merged = merged.drop_duplicates().dropna()

single_protein_merged = merged.groupby(['accession']).count()

single_protein_merged = single_protein_merged[single_protein_merged['annotation'] == 1]
single_protein_merged = single_protein_merged[single_protein_merged['location'] == 1]

single_protein_merged = merged[merged.accession.isin(single_protein_merged.index)]
single_protein_merged.to_csv("single_annotation_mapping.csv", index=False)

single_merged = single_protein_merged[['annotation', 'location']].drop_duplicates()
single_merged = single_merged.groupby('location').apply(lambda x: ';'.join(x['annotation']))
single_merged = single_merged.str.split(";", expand=True)
single_merged.to_csv("automatically_mapped_swissprot_deeploc_localizations_single.csv")

merged = merged[['annotation', 'location']].drop_duplicates()
merged = merged.groupby('location').apply(lambda x: ';'.join(x['annotation']))
merged = merged.str.split(";", expand=True)

merged.to_csv("automatically_mapped_swissprot_deeploc_localizations.csv")

