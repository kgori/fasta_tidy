import rich_click as click

def read_fasta_file(filename):
    sequences = {}
    seqname = None
    with open(filename) as fl:
        for line in fl:
            if line.startswith('>'):
                if seqname is not None:
                    sequences[seqname] = ''.join(sequences[seqname])
                seqname = line[1:].strip()
                sequences[seqname] = []
            else:
                if seqname is not None:
                    sequences[seqname].append(line.strip())
    if seqname is not None:
        sequences[seqname] = ''.join(sequences[seqname])
    return sequences

def write_fixed_length(outfile, seqdict, line_length=60):
    with open(outfile, 'w') as fl:
        for seqname, seq in seqdict.items():
            print('>' + seqname, file=fl)
            for i in range(0, len(seq), line_length):
                print(seq[i:i+line_length], file=fl)

@click.command()
@click.option("-i", "--infile", required=True, type=click.Path(exists=True), help="Input fasta file")
@click.option("-o", "--outfile", required=True, type=click.Path(), help="Output fasta file")
@click.option("-l", "--line-length", default=60, type=int, help="Line length for output fasta file")
def main(infile, outfile, line_length):
    sequences = read_fasta_file(infile)
    write_fixed_length(outfile, sequences, line_length)

if __name__ == '__main__':
    main()
