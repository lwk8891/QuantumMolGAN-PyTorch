import sparse_molecular_dataset
import sys

path = sys.argv[1]
data = sparse_molecular_dataset.SparseMolecularDataset()
data.load(path)
print(data.__dict__)
