import pandas as pd
import numpy as np
import os 
from ost import io

SCICORE_PDB_LOC = '/scicore/data/managed/PDB/latest/data/structures/divided/pdb'

os.chdir(SCICORE_PDB_LOC)

data = pd.read_csv('data_preprocessed.csv')

open

for pdb_id, chain in data[['PDB_ID','Chains']].head(100).to_numpy():

    # Find the right folder
    loc = f'{pdb_id[2,3]}/pdb{pdb_id}.ent.gz'

    # Load the PDB
    ent = io.loadPDB(loc)

    # Make a selection
    