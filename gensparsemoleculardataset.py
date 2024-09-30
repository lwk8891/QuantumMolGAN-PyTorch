from data.sparse_molecular_dataset import SparseMolecularDataset
import argparse
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--kekulization', default=True, action=argparse.BooleanOptionalAction, help='Kekulization')
    parser.add_argument('-y', '--add_hydrogen', default=False, action=argparse.BooleanOptionalAction, help='add hydrogen atoms')
    parser.add_argument('-a', '--validation_rate', type=float, default=0.1, help='the rate of the validation set')
    parser.add_argument('-t', '--test_rate', type=float, default=0.1, help='the rate of the test set')
    parser.add_argument('-n', '--natom', type=int, default=None, help='the maximum number of atoms to obtain SparseMolecularDataset')
    parser.add_argument('-o', '--output', type=str, default=None, help='the path of the output SparseMolecularDataset')
    parser.add_argument('source', type=str, help='the path of the sdf or smiles file to obtain SparseMolecularDataset')

    args = parser.parse_args()

    if args.output == None and args.natom == None:
        output_path = f'{os.path.splitext(args.source)[0]}.sparsedataset'
    elif args.output == None:
        output_path = f'{os.path.splitext(args.source)[0]}_{args.natom}nodes.sparsedataset'
    else:
        output_path = args.output

    moldata = SparseMolecularDataset()
    moldata.generate(args.source, args.kekulization, args.add_hydrogen, filters=lambda x: x.GetNumAtoms() <= args.natom, validation=args.validation_rate, test=args.test_rate)
    moldata.save(output_path)

if __name__ == '__main__':
    main()