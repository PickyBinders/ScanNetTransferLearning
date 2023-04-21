import pandas as pd
import numpy as np
import os 
from ost import io

SCICORE_PDB_LOC = '/scicore/data/managed/PDB/latest/data/structures/divided/pdb'

os.chdir(SCICORE_PDB_LOC)

data = pd.read_csv('data_preprocessed.csv')

f = open('test.txt','w')

for pdb_id, chain, labels in data[['PDB_ID','Chains', 'res_string']].head(100).to_numpy():

    # Find the right folder
    loc = f'{pdb_id[2,3]}/pdb{pdb_id}.ent.gz'

    # Load the PDB
    ent = io.loadPDB(loc)

    # Make a selection
    selection = ent.Select(f'chain={chain} and protein=true')

    # Write the PDB identifier in the file
    f.write(f'>{pdb_id}_{chain}')

    for index, residue, label in (selection.index, selection.residues, labels):
        f.write(f'{chain} {index} {residue} {label}')