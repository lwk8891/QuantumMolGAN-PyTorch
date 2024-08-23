from sparse_molecular_dataset import SparseMolecularDataset
import sys, os

if len(sys.argv) != 3:
  print('The number of the arguments is wrong!')
  exit(1)

in_filename = sys.argv[1]
atomnum = int(sys.argv[2])
data = SparseMolecularDataset()
if os.path.isfile(in_filename):
  if atomnum == 0:
    data.generate(in_filename)
    out_filename = f'{os.path.splitext(in_filename)[0]}.sparsedataset'
  else:
    data.generate(in_filename, filters=lambda x: x.GetNumAtoms() == atomnum)
    out_filename = f'{os.path.splitext(in_filename)[0]}_equal{atomnum}nodes.sparsedataset'
  data.save(out_filename)
else:
  print('There is no input file.')
