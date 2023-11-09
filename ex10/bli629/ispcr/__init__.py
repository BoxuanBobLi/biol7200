import subprocess

from .blastn import run_blastn, filter_blastn_results
from .identify_primers import idfp
from .extract_amp import examp

def step_one(primer_file: str, assembly_file: str) -> list[list[str]]:
    # 1. Run BLASTN
    blastn_output = run_blastn(primer_file, assembly_file)
    
    # 2. Filter results
    results = filter_blastn_results(blastn_output)
    
    # Convert the results to strings (in case we used float or int during processing)
    str_results = [[str(item) for item in sublist] for sublist in results]
    
    # Clear blast file after using it
    rmblastn = ["rm", "blastn_output.txt"]
    subprocess.run(rmblastn, check=True)
    
    return str_results


def step_two(sorted_hits: list[str], max_amplicon_size: int) -> list[tuple[list[str]]]:
    """
    Identify valid PCR amplicons based on the BLAST hits.
    """
    valid_amplicons = idfp(sorted_hits, max_amplicon_size)

    return valid_amplicons


def step_three(hit_pairs: list[tuple[list[str]]], assembly_file: str) -> str:
    """
    Extract sequences using seqtk based on the provided primer pair hits.
    """
    
    result = examp(hit_pairs, assembly_file)

    return result

