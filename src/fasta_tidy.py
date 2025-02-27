import rich_click as click
import itertools

def read_fasta_file(filename):
    with open(filename) as fl:
        groups = itertools.groupby(fl, key=lambda line: line.strip().startswith('>'))

        for is_header, group in groups:
            if is_header:
                header = next(group).strip()[1:]
            else:
                sequence = ''.join(line.strip() for line in group)
                yield header, sequence

def write_fixed_length(outfile, seq_iterator, line_length=60):
    with open(outfile, 'w') as fl:
        for header, sequence in seq_iterator:
            print('>' + header, file=fl)
            for i in range(0, len(sequence), line_length):
                print(sequence[i:i+line_length], file=fl)

@click.command(help="FASTA-TIDY: Rewrite ragged or single-line FASTA files to neat, line-wrapped FASTA files", no_args_is_help=True)
@click.option("-i", "--infile", required=True, type=click.Path(exists=True), help="Input fasta file")
@click.option("-o", "--outfile", required=True, type=click.Path(), help="Output fasta file")
@click.option("-l", "--line-length", default=60, type=int, help="Line length for output fasta file", show_default=True)
def main(infile, outfile, line_length):
    sequences = read_fasta_file(infile)
    write_fixed_length(outfile, sequences, line_length)

if __name__ == '__main__':
    main()
