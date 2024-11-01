from rdkit import Chem
import sys
import os

filename = sys.argv[1]
with open(filename, 'r') as f:
    lines = f.readlines()

filtered_smiles_list = []
for line in lines:
    mol = Chem.MolFromSmiles(line.strip())
    fragments = Chem.GetMolFrags(mol, asMols=True)
    filtered_fragments = [frag for frag in fragments if frag.GetNumAtoms() > 4]
    if len(filtered_fragments) == 1:
        filtered_smiles = Chem.MolToSmiles(filtered_fragments[0])
        if not filtered_smiles in filtered_smiles_list:
            filtered_smiles_list.append(filtered_smiles)

outputfilename = f"{os.path.splitext(filename)[0]}_fc_valid_unique.csv"
with open(outputfilename, 'w') as f:
    f.write("\n".join(filtered_smiles_list))

