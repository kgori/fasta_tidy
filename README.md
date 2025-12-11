fasta_tidy
==

Rewrite ragged or single-line FASTA files to neat, line-wrapped FASTA files

```
 Usage: fasta_tidy [OPTIONS]

 FASTA-TIDY: Rewrite ragged or single-line FASTA files to neat, line-wrapped FASTA files

 Options:
 *  --infile          -i  PATH     Input fasta file [required]
 *  --outfile         -o  PATH     Output fasta file [required]
    --line-length     -l  INTEGER  Line length for output fasta file [default: 60]
    --minimum-length  -m  INTEGER  Minimum sequence length to include [default: 0]
    --maximum-length  -x  INTEGER  Maximum sequence length to include [default: 2147483647]
    --sort            -s           Sort sequences by length (longest first)
    --help                         Show this message and exit.

```
