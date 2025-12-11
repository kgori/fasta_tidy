import rich_click as click
import itertools
import os
import tempfile

SAM_MAX_LEN=(2^31-1)

def read_fasta_file(filename, minlen=0, maxlen=SAM_MAX_LEN):
    with open(filename) as fl:
        groups = itertools.groupby(fl, key=lambda line: line.strip().startswith('>'))

        for is_header, group in groups:
            if is_header:
                header = next(group).strip()[1:]
            else:
                sequence = ''.join(line.strip() for line in group)
                l = len(sequence)
                if minlen <= l <= maxlen:
                    yield header, sequence

def write_fixed_length(outfile, seq_iterator, line_length=60):
    with open(outfile, 'w') as fl:
        for header, sequence in seq_iterator:
            print('>' + header, file=fl)
            for i in range(0, len(sequence), line_length):
                print(sequence[i:i+line_length], file=fl)

def write_sorted(outfile, seq_iterator, line_length=60):
    sortcache = []
    for header, sequence in seq_iterator:
        tmpfile = tempfile.NamedTemporaryFile(delete=False)
        tmpfile.close()
        sortcache.append((tmpfile.name, len(sequence)))
        write_fixed_length(tmpfile.name, [(header, sequence)], line_length)
    sortcache.sort(key=lambda x: x[1], reverse=True)
    with open(outfile, 'w') as fl:
        for filename, _ in sortcache:
            with open(filename) as inf:
                for line in inf:
                    fl.write(line)
            os.remove(filename)
                
def fasta_tidy(infile, outfile, line_length, minimum_length, maximum_length, sort):
    sequences = read_fasta_file(infile, minlen=minimum_length, maxlen=maximum_length)
    if sort:
        write_sorted(outfile, sequences, line_length)
    else:
        write_fixed_length(outfile, sequences, line_length)

@click.command(help="FASTA-TIDY: Rewrite ragged or single-line FASTA files to neat, line-wrapped FASTA files", no_args_is_help=True)
@click.option("-i", "--infile", required=True, type=click.Path(exists=True), help="Input fasta file")
@click.option("-o", "--outfile", required=True, type=click.Path(), help="Output fasta file")
@click.option("-l", "--line-length", default=60, type=int, help="Line length for output fasta file", show_default=True)
@click.option("-m", "--minimum-length", default=0, type=int, help="Minimum sequence length to include", show_default=True)
@click.option("-x", "--maximum-length", default=SAM_MAX_LEN, type=int, help="Maximum sequence length to include", show_default=True)
@click.option("-s", "--sort", is_flag=True, help="Sort sequences by length (longest first)")
def fasta_tidy_app(infile, outfile, line_length, minimum_length, maximum_length, sort):
    fasta_tidy(infile, outfile, line_length, minimum_length, maximum_length, sort)

if __name__ == '__main__':
    fasta_tidy_app()
