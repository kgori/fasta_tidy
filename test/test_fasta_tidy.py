import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from fasta_tidy import fasta_tidy

@pytest.fixture
def ragged_fasta_path():
    return os.path.join('test', 'data', 'ragged.fa')

@pytest.fixture
def neat20_fasta_path():
    return os.path.join('test', 'data', 'neat20.fa')

@pytest.fixture
def neat80_fasta_path():
    return os.path.join('test', 'data', 'neat80.fa')

def test_fasta_tidy_line_length_20(ragged_fasta_path, neat20_fasta_path):
    # Create a temporary output file
    output_path = 'test_output_20.fa'
    fasta_tidy(ragged_fasta_path, output_path, line_length=20)

    # Compare output file with expected neat20.fa
    with open(output_path, 'r') as file:
        output = file.read()
    with open(neat20_fasta_path, 'r') as file:
        expected = file.read()
    assert output == expected

    # Clean up the generated file
    os.remove(output_path)

def test_fasta_tidy_line_length_80(ragged_fasta_path, neat80_fasta_path):
    # Create a temporary output file
    output_path = 'test_output_80.fa'
    fasta_tidy(ragged_fasta_path, output_path, line_length=80)

    # Compare output file with expected neat80.fa
    with open(output_path, 'r') as file:
        output = file.read()
    with open(neat80_fasta_path, 'r') as file:
        expected = file.read()
    assert output == expected

    # Clean up the generated file
    os.remove(output_path)

