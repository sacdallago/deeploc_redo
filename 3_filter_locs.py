from pandas import read_csv

locs = read_csv('subcellular_localizations.csv')

evidence_codes = locs.evidence.unique()

# ECO:0000305 -- curator inference used in manual assertion -- IC
# ECO:0000250 -- sequence similarity evidence used in manual assertion -- ISS
# ECO:0000269 -- experimental evidence used in manual assertion -- EXP
# nan
# ECO:0000255 -- match to sequence model evidence used in manual assertion -- ISM
# ECO:0000303 -- author statement without traceable support used in manual assertion -- NAS

acceptable_evidence_code = 'ECO:0000269'
locs = locs[locs.evidence == acceptable_evidence_code]
locs.to_csv('evidence_subcellular_localizations.csv', header=True, index=False)

location_count = locs.groupby('location').size()
location_count.to_csv('evidence_count_subcellular_localizations.csv', header=True)
