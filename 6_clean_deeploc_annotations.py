#/!bin/python

from pandas import read_csv

annotations = read_csv("deeploc_annotations.txt", sep=" ", names=["accession", "annotation", "set"])
annotations['annotation'] = annotations['annotation'].str.split('-', expand=True)[0]
annotations['accession'] = annotations['accession'].str.slice(1)
annotations['accession'] = annotations['accession'].str.split('-', expand=True)[0]

annotations.to_csv('filtered_deeploc_annotations.csv', index=False)
